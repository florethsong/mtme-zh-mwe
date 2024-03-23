# -*- coding: utf-8 -*-
# @Time    : 2024/3/23 14:04
# @Author  : Huacheng Song and Hongzhi Xu
# @File    : mtmeMWE.py
# @Description :
'''
Based on the re-grouped WMT22 data, this script is used to compute normalized agerage scores and Kendall rank correlation coefficients
and to perform paired t-tests at both property and category level. Available parameter are list in metric_list (for 'metric'),
level_list (for 'level') , and mode_list_property as well as mode_list_category (for 'mode' corresponding to two levels.
The examples are provided in the end part.
'''

import json
import os
import shutil
import numpy as np
from mt_metrics_eval import data
from scipy.stats import ttest_rel


metric_list = ['metricx_xl_DA_2019-refA', 'metricx_xxl_DA_2019-refA',
               'metricx_xxl_MQM_2020-refA', 'BLEURT-20-refA', 'metricx_xl_MQM_2020-refA',
               'COMET-22-refA', 'COMET-20-refA', 'UniTE-refA', 'MS-COMET-22-refA', 'UniTE-ref-refA',
               'MATESE-refA', 'YiSi-1-refA', 'MEE4-refA', 'COMETKiwi-src', 'Cross-QE-src', 'COMET-QE-src',
               'BERTScore-refA', 'UniTE-src-src', 'MEE2-refA', 'MS-COMET-QE-22-src',
               'MATESE-QE-src', 'MEE-refA', 'f101spBLEU-refA', 'f200spBLEU-refA', 'chrF-refA',
               'BLEU-refA', 'HWTSC-TLM-src', 'HWTSC-Teacher-Sim-src',
               'KG-BERTScore-src', 'REUSE-src', 'SEScore-refA']

system_list = ['AISP-SJTU', 'bleu_bestmbr', 'bleurt_bestmbr', 'chrf_bestmbr',
                   'comet_bestmbr', 'DLUT', 'HuaweiTSC', 'JDExploreAcademy', 'Lan-Bridge',
                   'LanguageX', 'M2M100_1.2B-B4', 'NiuTrans', 'Online-A', 'Online-B', 'Online-G',
                   'Online-W', 'Online-Y', 'QUARTZ_TuneReranking', 'refB', 'refA']

level_list = ['property', 'category']

mode_list_property = ['with', 'without', 'only_ne', 'without_only_ne', 'only_mwe#', 'without_only_mwe#',
                      'mwe#+ne', 'without_mwe#+ne', 'with_ne', 'without_ne', 'with_mwe#', 'without_mwe#']

mode_list_category = ['NID', 'ION', 'IDI', 'CON', 'VID', 'VPC.semi', 'LVC.full', 'LVC.cause', 'MVC',
                    'PERSON', 'NORP', 'FAC', 'ORG', 'GPE', 'LOC', 'PRODUCT', 'EVENT',
                    'WORK_OF_ART', 'LAW', 'LANGUAGE', 'DATE', 'TIME', 'PERCENT', 'MONEY',
                    'QUANTITY', 'ORDINAL', 'CARDINAL', 'TER']

class MetaEvaluation():
    def __init__(self):
        self._prop_path = "./property level/"
        self._cat_path = "./category level/"
        self._dirin = "./raw_wmt22_zh-en/"
        self._dirout = "./wmt22/"
        self._id_list = []
        self._minmax_dict = {}

    def _listID(self) -> list[int]:
        if self.level == 'category':
            self.idpath = f'{self._cat_path}cat.json'
            with open (self.idpath, 'r', encoding='utf-8-sig') as fidcat:
                load_id_file = json.load(fidcat)
            for i in load_id_file[self.mode]:
                self._id_list.append(i['index'])
            return self._id_list
        elif self.level == 'property':
            self.idpath = f'{self._prop_path}{self.mode}.json'
            with open (self.idpath, 'r', encoding='utf-8-sig') as fidpro:
                load_id_file = json.load(fidpro)
            for i in load_id_file:
                self._id_list.append(i['index'])
            return self._id_list
        else:
            print('This level does not exist.')

    def _MinMax(self) -> dict[str:[int, int]]:
        for me in metric_list:
            self._minmax_dict[me] = []
        score_dir = f"{self._dirin}metric-scores/zh-en_all/"
        for f in os.listdir(score_dir):
            if 'refA' in f or 'src' in f:
                score_list = []
                with open(os.path.join(score_dir, f), 'r', encoding='utf-8') as fin:
                    f = f.replace('.seg.score', '')
                    for ssin in fin.read().strip().split('\n'):
                        m, s = ssin.split('\t')
                        if m != 'refA':
                            score_list.append(float(s))
                self._minmax_dict[f].append(min(score_list))
                self._minmax_dict[f].append(max(score_list))
        return self._minmax_dict

    def _groupSent(self):
        sent_path = ["documents/", "references/", "sources/", "system-outputs/zh-en/"]
        if len(self._id_list) > 0:
            for F in sent_path:
                in_path = f"{self._dirin}{F}"
                out_path = f"{self._dirout}{F}"
                if not os.path.exists(out_path):
                    os.makedirs(out_path)
                for f in os.listdir(in_path):
                    sent_list = []
                    with open(os.path.join(in_path, f), 'r', encoding='utf-8') as fin:
                        with open(os.path.join(out_path, f), 'w', encoding='utf-8') as fout:
                            sin = fin.read().strip().split('\n')
                            for i in self._id_list:
                                sent_list.append(sin[i])
                            for s in sent_list:
                                fout.write(f"{s}\n")
        else:
            print('The sentences cannot be grouped due to invaild sentence id list.')

    def _groupScore(self):
        sent_path = ["human-scores/", "metric-scores/zh-en_ref/", "metric-scores/zh-en_qe/", "metric-scores/zh-en/"]
        os.makedirs(self._dirout+sent_path[0])
        os.makedirs(self._dirout+sent_path[3])
        if len(self._id_list) > 0:
            for i, F in zip(range(3), sent_path[:3]):
                in_path = f"{self._dirin}{F}"
                for f in os.listdir(in_path):
                    with open(os.path.join(in_path, f), 'r', encoding='utf-8') as fin:
                        ssin = fin.read().strip().split('\n')
                        ssout = []
                        if i == 0:
                            out_path = f"{self._dirout}{F}"
                            for m in range(0, 37500, 1875):
                                with_list = []
                                metric_score = ssin[m:m + 1875]
                                for k in self._id_list:
                                    with_list.append(metric_score[k])
                                ssout = ssout + with_list
                        elif i == 1:
                            out_path = f"{self._dirout}{sent_path[3]}"
                            for m in range(0, 35625, 1875):
                                with_list = []
                                metric_score = ssin[m:m + 1875]
                                for k in self._id_list:
                                    with_list.append(metric_score[k])
                                ssout = ssout + with_list
                        elif i == 2:
                            out_path = f"{self._dirout}{sent_path[3]}"
                            for m in range(0, 37500, 1875):
                                with_list = []
                                metric_score = ssin[m:m + 1875]
                                for k in self._id_list:
                                    with_list.append(metric_score[k])
                                ssout = ssout + with_list
                    with open(os.path.join(out_path, f), 'w', encoding='utf-8') as fout:
                        for ss in ssout:
                            fout.write(f"{ss}\n")
            if self.mode in ["LAW", "ION"]:
                sys_domain = f"{self._dirin}human-score_sd-ecommerce/"
            elif self.mode in ["EVENT", "LAW", "LVC.cause", "NID", "NORP", "ORG", "PERSON, PRODUCT", "QUANTITY, TER", "WORK_OF_ART"]:
                sys_domain = f"{self._dirin}human-score_sd-conversation/"
            elif self.mode in ["LANGUAGE", "PRODUCT"]:
                sys_domain = f"{self._dirin}human-score_sd-news/"
            elif self.mode == "NORP":
                sys_domain = f"{self._dirin}human-score_sd-social/"
            else:
                sys_domain = f"{self._dirin}human-score_sd/"
            for sd in os.listdir(sys_domain):
                shutil.copy(sys_domain+sd, self._dirout+sent_path[0])
        else:
            print('The sentences cannot be grouped due to invaild sentence id list.')

    def constructGroup(self, level:str=None, mode:str=None):
        self.level = level
        self.mode = mode
        shutil.rmtree(self._dirout)
        os.mkdir(self._dirout)
        self._id_list = self._listID()
        try:
            self._groupScore()
            self._groupSent()
        except Exception as e:
            print(e)

    def NormalizedAgerageScore(self, metric: str=None):
        score_path = f"{self._dirout}metric-scores/zh-en/"
        for f in os.listdir(score_path):
            metricscore_dic = {}
            if metric in f:
                self._MinMax()
                with open(os.path.join(score_path, f), 'r', encoding='utf-8') as fin:
                    for ssin in fin.read().strip().split('\n'):
                        l = []
                        m, s = ssin.split('\t')
                        if m in metricscore_dic.keys():
                            a = metricscore_dic[m]
                            a.append(float(s))
                            metricscore_dic[m] = a
                        else:
                            l.append(float(s))
                            metricscore_dic[m] = l
                sysavg_list = []
                for k, v in metricscore_dic.items():
                    v_list = []
                    if k != 'refA':
                        for x in v:
                            x = float(x - self._minmax_dict[metric][0]) / (self._minmax_dict[metric][1] - self._minmax_dict[metric][0])
                            v_list.append(x)
                        sys_avg = sum(v_list) / len(v_list)
                        sysavg_list.append(sys_avg)
                metric_avg = sum(sysavg_list) / len(sysavg_list)
                return metric_avg

    def Kendall(self, metric: str=None):
        evs = data.EvalSet('wmt22', 'zh-en', read_stored_metric_scores=True, path="./")
        mqm_scores = evs.Scores('seg', 'mqm')
        qm_sys = set(mqm_scores) - evs.human_sys_names
        qm_sys_bp = qm_sys | {'refB'}
        scores = evs.Scores('seg', scorer=metric)
        mqm_bp = evs.Correlation(mqm_scores, scores, qm_sys_bp)
        kendall_cor = f"{mqm_bp.Kendall()[0]:f}"
        # print(f'The Kendall correlation between human and {metric} evaluations is {kendall_cor}')
        return kendall_cor

def PairedTtest(var1: list=None, var2: list=None):
    left_array = np.array(var1)
    right_array = np.array(var2)
    tstat, pval = ttest_rel(a=left_array, b=right_array, alternative="two-sided")
    result = f"{tstat}\t{pval}"
    return result


if __name__ == '__main__':
    level = 'category'
    mode = 'NID'
    metric = 'metricx_xl_DA_2019-refA'

    a = MetaEvaluation()#necessary
    a.constructGroup(level, mode)#necessary

    print(a.Kendall(metric))
    print(a.NormalizedAgerageScore(metric))
    # --------------------------------------------
    with_kc = [0.388818, 0.386236, 0.416837, 0.363453, 0.414062, 0.414519, 0.333788, 0.343455, 0.325034, 0.34862, 0.373301, 0.303225, 0.206814, 0.356068, 0.355095, 0.348174, 0.313525, 0.319269, 0.209278, 0.270855, 0.317408, 0.16514, 0.150304, 0.147244, 0.163226, 0.14458, 0.104342, 0.280869, 0.197746, 0.121482, 0.305426]
    without_kc = [0.34712, 0.338765, 0.378088, 0.313691, 0.366381, 0.397466, 0.290591, 0.365762, 0.330874, 0.36133, 0.346697, 0.263243, 0.213142, 0.306421, 0.292128, 0.27, 0.287965, 0.336689, 0.213048, 0.215848, 0.289654, 0.157009, 0.170273, 0.165237, 0.16141, 0.175512, 0.042246, 0.144098, 0.127337, 0.096412, 0.306112]
    print(PairedTtest(with_kc, without_kc))