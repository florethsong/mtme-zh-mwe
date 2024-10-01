# mtme-zh-mwe
---
<!-- Copyright [19 Mar 2024] [florethsong]  

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.-->

The dataset of WMT22 Metrics Shared Task extended with annotations of 28 types of Chinese Multiword Expressions (MWEs)
--

:pushpin:**9 types of non-NE MWE (MWEs#)**: noun-headed idiom (NID), separable word (or ionized word) (ION), four-character idiom (IDI), special construction (CON), verb-headed idiom (VID), semi non-compositional verb-particle construction (VPC.semi), light verb construction with bleached verb (LVC.full), light verb construction with causative verb (LVC.cause), and multi-verb construction (MVC) 
  
:pushpin:**19 types of named entities (NEs)**: person name (PERSON), nationality, religious, political or ethnic group (NORP), facility (FAC), organization (ORG), geopolitical entity (GPE), location (LOC), product (PRODUCT), event (EVENT), work of art (WORK_OF_ART, LAW), language (LANGUAGE), date (DATE), time (TIME), percent (PERCENT), money (MONEY), quantity (QUANTITY), ordinal (ORDINAL), cardinal (CARDINAL), terminology (TER)


### :card_index_dividers: Description of file structure
```
.
│  all.json
'''
Annotation results of all Chinese MWEs in the WMT22 zh-en source text (1,875 sentences) (Freitag et al., 2022),
with 'index' denoting the sentence index in the original data (starting from 0),
'property' denoting the presence of MWEs# or NEs, items in 'catogory' denoting the specific
type, position , and content of present MWEs.
'''
│  cat_list.json  # List of all annotated Chinese MWE items grouped by categories (non-deduplicated).
│  mtmeMWE.py  # Script of three statistical methods at both property and category level. Examples are provided in the file.
│  
├─#dic  # Dictionary exploited for the annotation of MWE#.
│      dic_CDI_35458.txt  # A Comprehensive Dictionary of Chinese/English Idioms (Zhang and Zhang, 2014)
│      dic_ID10M_dev_372.txt 
│      dic_ID10M_test_80.txt
│      dic_ID10M_train_1835.txt  # ID10M dataset (Tedeschi et al., 2022)
│      dic_PARSEME_4827.json
│      dic_PARSEME_4827.txt  # PARSEME 1.3 (zh) (Savary et al., 2023)
│      dic_total_39978.json
│      dic_total_39978.txt
│      
├─category level  # Annotation results grouped by MWE categories.
│      cat.json
│      
├─property level  # Annotation results grouped by MWE# and NE presence.
│      mwe#+ne.json
│      only_mwe#.json
│      only_ne.json
│      with.json
│      without.json
│      without_mwe#+ne.json
│      without_mwe#.json
│      without_ne.json
│      without_only_mwe#.json
│      without_only_ne.json
│      with_mwe#.json
│      with_ne.json
│      
└─raw_wmt22  # Original dataset from WMT22 Metric Sharted Task.
    ├─documents
    │      zh-en.docs
    │      
    ├─human-scores
    │      zh-en.mqm.seg.score
    │      zh-en.wmt-appraise-z.seg.score
    │      zh-en.wmt-appraise.seg.score
    │      zh-en.wmt-z.seg.score
    │      zh-en.wmt.seg.score
    │      
    ├─human-score_sd
    │      zh-en.mqm.domain.score
    │      zh-en.mqm.sys.score
    │      zh-en.wmt-appraise-z.sys.score
    │      zh-en.wmt-appraise.domain.score
    │      zh-en.wmt-appraise.sys.score
    │      zh-en.wmt-z.domain.score
    │      zh-en.wmt-z.sys.score
    │      zh-en.wmt.domain.score
    │      zh-en.wmt.sys.score
    │      
    ├─human-score_sd-conversation
    │      zh-en.mqm.domain.score
    │      zh-en.mqm.sys.score
    │      zh-en.wmt-appraise.sys.score
    │      zh-en.wmt-z.domain.score
    │      zh-en.wmt-z.sys.score
    │      zh-en.wmt.domain.score
    │      zh-en.wmt.sys.score
    │      
    ├─human-score_sd-ecommerce
    │      zh-en.mqm.domain.score
    │      zh-en.mqm.sys.score
    │      zh-en.wmt-appraise-z.sys.score
    │      zh-en.wmt-appraise.domain.score
    │      zh-en.wmt-appraise.sys.score
    │      zh-en.wmt-z.domain.score
    │      zh-en.wmt-z.sys.score
    │      zh-en.wmt.domain.score
    │      zh-en.wmt.sys.score
    │      
    ├─human-score_sd-news
    │      zh-en.mqm.domain.score
    │      zh-en.mqm.sys.score
    │      zh-en.wmt-appraise-z.sys.score
    │      zh-en.wmt-appraise.domain.score
    │      zh-en.wmt-appraise.sys.score
    │      zh-en.wmt-z.domain.score
    │      zh-en.wmt-z.sys.score
    │      zh-en.wmt.domain.score
    │      zh-en.wmt.sys.score
    │      
    ├─human-score_sd-social
    │      zh-en.mqm.domain.score
    │      zh-en.mqm.sys.score
    │      zh-en.wmt-appraise-z.sys.score
    │      zh-en.wmt-appraise.domain.score
    │      zh-en.wmt-appraise.sys.score
    │      zh-en.wmt-z.domain.score
    │      zh-en.wmt-z.sys.score
    │      zh-en.wmt.domain.score
    │      zh-en.wmt.sys.score
    │      
    ├─metric-scores
    │  ├─zh-en_all
    │  │      BERTScore-refA.seg.score
    │  │      BERTScore-refB.seg.score
    │  │      BLEU-refA.seg.score
    │  │      BLEU-refB.seg.score
    │  │      BLEURT-20-refA.seg.score
    │  │      BLEURT-20-refB.seg.score
    │  │      chrF-refA.seg.score
    │  │      chrF-refB.seg.score
    │  │      COMET-20-refA.seg.score
    │  │      COMET-20-refB.seg.score
    │  │      COMET-22-refA.seg.score
    │  │      COMET-22-refB.seg.score
    │  │      COMET-QE-src.seg.score
    │  │      COMETKiwi-src.seg.score
    │  │      Cross-QE-src.seg.score
    │  │      f101spBLEU-refA.seg.score
    │  │      f101spBLEU-refB.seg.score
    │  │      f200spBLEU-refA.seg.score
    │  │      f200spBLEU-refB.seg.score
    │  │      HWTSC-Teacher-Sim-src.seg.score
    │  │      HWTSC-TLM-src.seg.score
    │  │      KG-BERTScore-src.seg.score
    │  │      MATESE-QE-src.seg.score
    │  │      MATESE-refA.seg.score
    │  │      MATESE-refB.seg.score
    │  │      MEE-refA.seg.score
    │  │      MEE-refB.seg.score
    │  │      MEE2-refA.seg.score
    │  │      MEE2-refB.seg.score
    │  │      MEE4-refA.seg.score
    │  │      MEE4-refB.seg.score
    │  │      metricx_xl_DA_2019-refA.seg.score
    │  │      metricx_xl_DA_2019-refB.seg.score
    │  │      MS-COMET-22-refA.seg.score
    │  │      MS-COMET-22-refB.seg.score
    │  │      MS-COMET-QE-22-src.seg.score
    │  │      REUSE-src.seg.score
    │  │      SEScore-refA.seg.score
    │  │      SEScore-refB.seg.score
    │  │      UniTE-ref-refA.seg.score
    │  │      UniTE-ref-refB.seg.score
    │  │      UniTE-refA.seg.score
    │  │      UniTE-refB.seg.score
    │  │      UniTE-src-src.seg.score
    │  │      YiSi-1-refA.seg.score
    │  │      YiSi-1-refB.seg.score
    │  │      
    │  ├─zh-en_qe
    │  │      COMET-QE-src.seg.score
    │  │      COMETKiwi-src.seg.score
    │  │      Cross-QE-src.seg.score
    │  │      HWTSC-Teacher-Sim-src.seg.score
    │  │      HWTSC-TLM-src.seg.score
    │  │      KG-BERTScore-src.seg.score
    │  │      MATESE-QE-src.seg.score
    │  │      MS-COMET-QE-22-src.seg.score
    │  │      REUSE-src.seg.score
    │  │      UniTE-src-src.seg.score
    │  │      
    │  └─zh-en_ref
    │          BERTScore-refA.seg.score
    │          BERTScore-refB.seg.score
    │          BLEU-refA.seg.score
    │          BLEU-refB.seg.score
    │          BLEURT-20-refA.seg.score
    │          BLEURT-20-refB.seg.score
    │          chrF-refA.seg.score
    │          chrF-refB.seg.score
    │          COMET-20-refA.seg.score
    │          COMET-20-refB.seg.score
    │          COMET-22-refA.seg.score
    │          COMET-22-refB.seg.score
    │          f101spBLEU-refA.seg.score
    │          f101spBLEU-refB.seg.score
    │          f200spBLEU-refA.seg.score
    │          f200spBLEU-refB.seg.score
    │          MATESE-refA.seg.score
    │          MATESE-refB.seg.score
    │          MEE-refA.seg.score
    │          MEE-refB.seg.score
    │          MEE2-refA.seg.score
    │          MEE2-refB.seg.score
    │          MEE4-refA.seg.score
    │          MEE4-refB.seg.score
    │          metricx_xl_DA_2019-refA.seg.score
    │          metricx_xl_DA_2019-refB.seg.score
    │          MS-COMET-22-refA.seg.score
    │          MS-COMET-22-refB.seg.score
    │          SEScore-refA.seg.score
    │          SEScore-refB.seg.score
    │          UniTE-ref-refA.seg.score
    │          UniTE-ref-refB.seg.score
    │          UniTE-refA.seg.score
    │          UniTE-refB.seg.score
    │          YiSi-1-refA.seg.score
    │          YiSi-1-refB.seg.score
    │          
    ├─references
    │      zh-en.refA.txt
    │      zh-en.refB.txt
    │      
    ├─sources
    │      zh-en.txt
    │      
    └─system-outputs
        └─zh-en
                AISP-SJTU.txt
                bleurt_bestmbr.txt
                bleu_bestmbr.txt
                chrf_bestmbr.txt
                comet_bestmbr.txt
                DLUT.txt
                HuaweiTSC.txt
                JDExploreAcademy.txt
                Lan-Bridge.txt
                LanguageX.txt
                M2M100_1.2B-B4.txt
                NiuTrans.txt
                Online-A.txt
                Online-B.txt
                Online-G.txt
                Online-W.txt
                Online-Y.txt
                QUARTZ_TuneReranking.txt
                refA.txt
                refB.txt
```

## Citation
Please cite the following paper if it is helpful to your work :)!
```
@inproceedings{song-xu-2024-benchmarking,
    title = "Benchmarking the Performance of Machine Translation Evaluation Metrics with {C}hinese Multiword Expressions",
    author = "Song, Huacheng  and
      Xu, Hongzhi",
    editor = "Calzolari, Nicoletta  and
      Kan, Min-Yen  and
      Hoste, Veronique  and
      Lenci, Alessandro  and
      Sakti, Sakriani  and
      Xue, Nianwen",
    booktitle = "Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)",
    month = may,
    year = "2024",
    address = "Torino, Italia",
    publisher = "ELRA and ICCL",
    url = "https://aclanthology.org/2024.lrec-main.198",
    pages = "2204--2216",
}
```
P.S. We publish this Chinese MWE-annotated dataset in our work above which focuses on the meta-evaluation of machine translation automatic evaluation metrics from the perspective of MWEs. Another work of ours tightly following it, also built on this extended dataset, pays more effort to a full evaluation of machine translation systems on rendering Chinese MWEs into English. If you are interested, you can find more details at: https://github.com/florethsong/mte-zh-mwe.


## References
Markus Freitag, Ricardo Rei, Nitika Mathur, Chikiu Lo, Craig Stewart, Eleftherios Avramidis, Tom Kocmi, George Foster, Alon Lavie, and André F. T. Martins. 2022. [Results of WMT22 metrics shared task: Stop using BLEU - neural metrics are better and more robust](https://aclanthology.org/2022.wmt-1.2). In Proceedings of the Seventh Conference on Machine Translation (WMT), pages 46–68, Abu Dhabi, United Arab Emirates (Hybrid). Association for Computational Linguistics.  

Agata Savary, Cherifa Ben Khelil, Carlos Ramisch, Voula Giouli, Verginica Barbu Mititelu, Najet Hadj Mohamed, Cvetana Krstev, Chaya Liebeskind, Hongzhi Xu, Sara Stymne, Tunga
Güngör, Thomas Pickard, Bruno Guillaume, Eduard Bejček, Archna Bhatia, Marie Candito, Polona Gantar, Uxoa Iñurrieta, Albert Gatt, Jolanta Kovalevskaite, Timm Lichte, Nikola Ljubešić, Johanna Monti, Carla Parra Escartín, Mehrnoush Shamsfard, Ivelina Stoyanova, Veronika Vincze, and Abigail Walsh. 2023. [PARSEME corpus release 1.3](https://doi.org/10.18653/v1/2023.mwe-1.6). In Proceedings of the 19th Workshop on Multiword Expressions (MWE 2023), pages 24–35, Dubrovnik, Croatia. Association for Computational Linguistics.  

Simone Tedeschi, Federico Martelli, and Roberto Navigli. 2022. [ID10M: Idiom identification in 10 languages](https://aclanthology.org/2022.findings-naacl.208). In Findings of the Association for Computational Linguistics: NAACL 2022, pages 2715–2726, Seattle, United States. Association for Computational Linguistics.

Ralph Weischedel, Martha Palmer, Mitchell Marcus, Eduard Hovy, Sameer Pradhan, Lance Ramshaw, Ni-anwen Xue, Ann Taylor, Jeff Kaufman, Michelle Franchini, et al. 2012. [Ontonotes release 5.0 with ontonotes db tool v0. 999 beta](https://catalog.ldc.upenn.edu/docs/LDC2013T19/OntoNotes-Release-5.0.pdf). Linguistic Data Consortium.

Xueying Zhang and Hui Zhang. 2014. [A Comprehensive Dictionary of Chinese/English Idioms with English/Chinese Translations](http://www.tup.com.cn/en/bookbrief.html?id=05130701). Tsinghua University Press, Beijing.
