#! /usr/bin/env python
#-*- coding: utf-8 -*-

JPY_news = {'日元', '日本央行', '(日)瑞穗实业银行', '(日)东京三菱日联', '(日)野村证券',
            '日元相关'}

JPY_norm = {'(日)外汇储备', '(日)银行信贷', '(日)央行短观经济调查', '(日)领先指标',
            '(日)消费者信心指数', '(日)核心机械订单', '(日)经济观察家调查报告',
            '(日)受薪家庭支出', '(日)失业率', '(日)劳动现金收入', '(日)周资金流动数据',
            '(日)经常帐', '(日)贸易帐', '(日)工业产出', '(日)零售销售', '(日)大型零售商销售',
            '(日)第三产业活动指数', '(日)所有产业活动指数', '(日)企业破产', '(日)机床订单',
            '(日)GDP', '(日)企业商品物价指数', '(日)CPI', '(日)营建订单', '(日)新屋开工',
            '(日)家庭消费者信心指数', '(日)货币供应', '(日)路透短观经济调查',
            '(日)制造业PMI', '(日)基础货币', '(日)企业服务价格指数', '(日)企业资本支出'}

JPY_analy = {'穆迪', '标普评级', '惠誉', '专家评论', '机构评论', '投资报告', '国内媒体',
            '国外媒体', '推荐', '头条', 'IMM持仓', 'CFTC持仓报告', 'LME持仓报告', '基本分析',
            '技术分析', '心理分析', '分析评论', '指标预测', '指标解读', '利率决定',
            '货币政策解读', '货币政策预期', '汇率预期', '市场传闻', '投机情绪', '深度报道',
            '经济分析', '市场反应', '外汇即时解盘', '观点'}


CHF_news = {'瑞郎', '瑞士央行', '(瑞)瑞银集团', '(瑞)瑞信', '瑞士满汇银行(MIG)', '瑞郎相关'}

CHF_norm = {'(瑞)失业率', '(瑞)零售销售', '(瑞)工业产出', '(瑞)SVME制造业采购经理人指数',
            '(瑞)UBS消费指数', '(瑞)消费者信心指数', '(瑞)非农就业人数', '(瑞)贸易帐',
            '(瑞)ZEW投资者信心指数', '(瑞)GDP', '(瑞)CPI', '(瑞)PPI', '(瑞)KOF领先指标'}

CHF_analy = {'穆迪', '标普评级', '惠誉', '专家评论', '机构评论', '投资报告', '国内媒体',
            '国外媒体', '推荐', '头条', 'IMM持仓', 'CFTC持仓报告', 'LME持仓报告', '基本分析',
            '技术分析', '心理分析', '分析评论', '指标预测', '指标解读', '利率决定',
            '货币政策解读', '货币政策预期', '汇率预期', '市场传闻', '投机情绪', '深度报道',
            '经济分析', '市场反应', '外汇即时解盘', '观点'}

USD_news = {'美元', '美联储', '(美)美国运通银行', '(美)摩根大通', '(美)摩根士丹利',
            '(美)高盛', '(美)花旗集团', '(美)美国银行', '(美)布朗兄弟哈里曼', '富国银行',
            '美元相关', '美联储决议', '美联储主席', '美联储证词', '美元相关'}

USD_norm = {'(美)非农就业人数', '(美)成屋签约销售', '(美)ISM制造业指数(美)', 'ISM非制造业指数',
            '(美)谘商会消费者信心指数', '(美)密歇根大学消费者信心', '(美)零售销售',
            '(美)个人支出', '(美)工业产出', '(美)工厂订单', '(美)耐用品订单',
            '(美)产能利用率', '(美)营建许可', '(美)新屋开工', '(美)成屋销售',
            '(美)经常帐', '(美)贸易帐', '(美)商业库存', '(美)劳动生产率', '(美)劳工成本',
            '(美)初请失业金人数', '(美)堪萨斯联储制造业指数', '(美)纽约联储制造业调查',
            '(美)达拉斯联储调查', '(美)里奇蒙德联储制造业指数', '(美)费城联储商业前景调查',
            '(美)芝加哥联储全国活动指数', '(美)芝加哥采购经理人指数', '(美)消费信贷',
            '(美)资本净流入', '(美)财政预算', '(美)IBD消费者信心指数', '(美)挑战者企业裁员',
            '(美)抵押贷款市场综合指数', '(美)EIA/API石油数据报告', '(美)GDP', '(美)CPI',
            '(美)PPI','(美)NAHB房价指数', '(美)失业率', '(美)新屋销售',
            '(美)UFJ银行商业景气指数', '(美)个人消费支出物价指数', '(美)ADP就业',
            '(美)批发销售', '(美)批发库存', '(美)进出口物价指数', '(美)S&P/CS大城市房价指数',
            '(美)谘商会领先指标', '(美)Markit制造业PMI', '(美)美联储LMCI'}

USD_analy = {'穆迪', '标普评级', '惠誉', '专家评论', '机构评论', '投资报告', '国内媒体',
            '国外媒体', '推荐', '头条', 'IMM持仓', 'CFTC持仓报告', 'LME持仓报告', '基本分析',
            '技术分析', '心理分析', '分析评论', '指标预测', '指标解读', '利率决定',
            '货币政策解读', '货币政策预期', '汇率预期', '市场传闻', '投机情绪', '深度报道',
            '经济分析', '市场反应', '外汇即时解盘', '观点'}


EUR_news = {'欧元', '(法)农业信贷银行', '(意)意大利联合信贷银行', '丹麦盛宝银行',
            '(法)东方汇理银行', '法国外贸银行', '(德)德意志银行', '(法)兴业银行',
            '荷兰国际集团 (ING)', '欧洲央行', '(法)里昂信贷银行', '(加)TD证券',
            '(德)商业银行', '(法)法国巴黎银行', '(德)西德意志银行', '欧洲央行决议及新闻发布会',
            '欧元相关'}

EUR_norm = {'(德)ILO就业人数', '(德)失业率(官方)', '(德)劳工成本', '(德)经常帐',
            '(德)贸易帐', '(德)PPI', '(德)批发物价指数', '(德)工业产出', '(德)制造业订单',
            '(德)IFO商业景气指数', '(德)GFK消费者信心指数', '(德)财政预算',
            '(德)ZEW经济景气指数', '(德)制造业采购经理人指数', '(德)服务业采购经理人指数',
            '(德)CPI', '(德)GDP', '(德)零售销售', '(德)进口物价指数', '(法)家庭消费支出',
            '(法)消费者信心指数', '(法)Insee商业信心指数', '(法)PPI', '(法)工业产出',
            '(法)非农就业人口', '(法)失业率', '(法)新屋开工', '(法)经常帐',
            '(法)BOF商业信心指数', '(法)制造业采购经理人指数', '(法)服务业采购经理人指数',
            '(法)政府预算', '(法)贸易帐', '(法)CPI', '(法)GDP', '(意)工业销售',
            '(意)工业产出', '(意)贸易帐', '(意)零售销售', '(意)政府预算', '(意)失业率',
            '(意)ISAE商业信心指数', '(意)制造业采购经理人指数', '(意)服务业采购经理人指数',
            '(意)GDP', '(意)CPI', '(意)PPI', '(意)ISTAT消费者信心指数'}

EUR_analy = {'穆迪', '标普评级', '惠誉', '专家评论', '机构评论', '投资报告', '国内媒体',
            '国外媒体', '推荐', '头条', 'IMM持仓', 'CFTC持仓报告', 'LME持仓报告', '基本分析',
            '技术分析', '心理分析', '分析评论', '指标预测', '指标解读', '利率决定',
            '货币政策解读', '货币政策预期', '汇率预期', '市场传闻', '投机情绪', '深度报道',
            '经济分析', '市场反应', '外汇即时解盘', '观点'}


GBP_news = {'英镑', '英国央行', '(英)巴克莱银行', '(英)渣打银行', '(英)皇家苏格兰银行',
            '(英)汇丰控股', '劳埃德银行', '英镑相关'}

GBP_norm = {'(英)服务业采购经理人指数', '(英)制造业采购经理人指数', '(英)Halifax房价指数',
            '(英)RICS房价指数', '(英)DCLG房价指数', '(英)Rightmove房价指数',
            '(英)Nationwide房价指数', '(英)Hometrack房价指数', '(英)BRC零售销售',
            '(英)BRC商店物价指数', '(英)NIESR', 'GDP预估', '(英)失业率', '(英)零售物价指数',
            '(英)零售销售', '(英)工业产出', '(英)政府收支短差', '(英)贸易帐', '(英)经常帐',
            '(英)消费信贷', '(英)M4货币供应', '(英)BBA抵押贷款', '(英)GFK消费者信心指数',
            '(英)CBI制造业趋势调查', '(英)CBI零售业调查', '(英)GDP', '(英)CPI', '(英)PPI',
            '(英)建筑业采购经理人指数', '(英)CML', '抵押贷款', '(英)BSA', '抵押贷款',
            '(英)Nationwide消费者信心指数', '(英)央行抵押贷款许可'}

GBP_analy = {'穆迪', '标普评级', '惠誉', '专家评论', '机构评论', '投资报告', '国内媒体',
            '国外媒体', '推荐', '头条', 'IMM持仓', 'CFTC持仓报告', 'LME持仓报告', '基本分析',
            '技术分析', '心理分析', '分析评论', '指标预测', '指标解读', '利率决定',
            '货币政策解读', '货币政策预期', '汇率预期', '市场传闻', '投机情绪', '深度报道',
            '经济分析', '市场反应', '外汇即时解盘', '观点'}


AUD_news = {'澳元', '澳洲联储', '(澳)澳新银行', '(澳)澳洲国民银行', '(澳)西太平洋银行',
            '(澳)澳洲联邦银行','澳元相关'}

AUD_norm = {'(澳)经常帐', '(澳)房屋价格指数', '(澳)营建许可', '(澳)房屋贷款',
            '(澳)薪资价格指数', '(澳)平均周薪', '(澳)失业率', '(澳)NAB商业景气指数',
            '(澳)AIG服务业表现指数', '(澳)ANZ招聘广告', '(澳)西太平洋/墨尔本消费者信心指数',
            '(澳)西太平洋领先指标', '(澳)DEWR熟练工职位空缺', '(澳)GDP', '(澳)CPI',
            '(澳)PPI', '(澳)出口物价指数', '(澳)进口物价指数', '(澳)AIG建筑业表现指数',
            '(澳)澳大利亚个人/商业融资', '(澳)TD-MI通胀指数', '(澳)私营企业贷款',
            '(澳)零售销售', '(澳)AIG/CBA服务业表现指数', '(澳)贸易帐',
            '(澳)AIG/PWC制造业表现指数', '(澳)谘商会领先指标', '(澳)营建完工', '(澳)企业获利'}

AUD_analy = {'穆迪', '标普评级', '惠誉', '专家评论', '机构评论', '投资报告', '国内媒体',
            '国外媒体', '推荐', '头条', 'IMM持仓', 'CFTC持仓报告', 'LME持仓报告', '基本分析',
            '技术分析', '心理分析', '分析评论', '指标预测', '指标解读', '利率决定',
            '货币政策解读', '货币政策预期', '汇率预期', '市场传闻', '投机情绪', '深度报道',
            '经济分析', '市场反应', '外汇即时解盘', '观点'}


CAD_news = {'加元', '加拿大央行', '(加)加拿大皇家银行', '(加)加拿大帝国商业银行',
            '(加)蒙特利尔银行', '(加)多伦多道明银行', '(加)丰业银行', '加元相关'}

CAD_norm = {'(加)原材料物价指数', '(加)GDP', '(加)新屋价格指数', '(加)失业率',
            '(加)营建许可', '(加)新屋开工', '(加)贸易帐', '(加)经常帐', '(加)零售销售',
            '(加)领先指标', '(加)批发销售', '(加)劳动生产力', '(加)工业产能利用率',
            '(加)资金流动', '(加)IVEY采购经理人指数', '(加)外汇储备', '(加)CPI', '(加)PPI',
            '(加)RBC制造业PMI', '(加)制造业装船'}

CAD_analy = {'穆迪', '标普评级', '惠誉', '专家评论', '机构评论', '投资报告', '国内媒体',
            '国外媒体', '推荐', '头条', 'IMM持仓', 'CFTC持仓报告', 'LME持仓报告', '基本分析',
            '技术分析', '心理分析', '分析评论', '指标预测', '指标解读', '利率决定',
            '货币政策解读', '货币政策预期', '汇率预期', '市场传闻', '投机情绪', '深度报道',
            '经济分析', '市场反应', '外汇即时解盘', '观点'}


RMB_news = {'人民币', '中国央行', '广东发展银行', '浦东发展银行', '中国银行', '工商银行',
            '建设银行', '交通银行', '中国农业银行', '人民币相关'}

RMB_norm = {'(中)主要工业产品产量', '(中)全社会固定资产投资', '(中)城镇固定资产投资',
            '(中)工业增加值', '(中)企业景气指数', '(中)企业家信心指数', '(中)M2货币供应',
            '(中)外汇储备', '(中)经常帐', '(中)贸易帐', '(中)外商直接投资',
            '(中)汇丰采购经理人指数', '(中)官方采购经理人指数', '(中)GDP', '(中)CPI',
            '(中)PPI', '(中)社会消费品零售总额', '(中)房地产开发投资', '(中)工业企业利润',
            '(中)谘商会领先指标'}

RMB_analy = {'穆迪', '标普评级', '惠誉', '专家评论', '机构评论', '投资报告', '国内媒体',
            '国外媒体', '推荐', '头条', 'IMM持仓', 'CFTC持仓报告', 'LME持仓报告', '基本分析',
            '技术分析', '心理分析', '分析评论', '指标预测', '指标解读', '利率决定',
            '货币政策解读', '货币政策预期', '汇率预期', '市场传闻', '投机情绪', '深度报道',
            '经济分析', '市场反应', '外汇即时解盘', '观点'}


gold = {'黄金', '黄金交易策略', '黄金交易提醒'}

silver = {'白银'}

crude = {'原油'}

bond = {'债券'}

kinds_flag = [JPY_news, JPY_norm, JPY_analy, CHF_news, CHF_norm, CHF_analy,
                USD_news, USD_norm, USD_analy, EUR_news, EUR_norm, EUR_analy,
                GBP_news, GBP_norm, GBP_analy, AUD_news, AUD_norm, AUD_analy,
                CAD_news, CAD_norm, CAD_analy, RMB_news, RMB_norm, RMB_analy,
                gold, silver, crude, bond]
