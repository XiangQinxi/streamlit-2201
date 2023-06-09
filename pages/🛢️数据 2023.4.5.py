import streamlit as st
from streamlit_extras.let_it_rain import rain


with st.sidebar:
    from streamlit_extras.colored_header import colored_header

    rain(
        emoji="🍭",
        font_size=32,
        falling_speed=8,
    )

    colored_header(
        label="数据 2023年4月5日",
        description="记录七中信息数据",
        color_name="yellow-70",
    )

st.markdown(
    """
# 数据 2023.4.25
## 基本信息
邵阳市第十五中学，成立于`2015`年，位于`湖南省邵阳市`，宗旨和业务范围是“`实施中学教育，促进基础教育发展初中义务教育`”。该事业单位开办资金100万。

## 营运状况
邵阳市第十五中学参与招投标项目4次

| 序号	 | 发布日期	       | 标题	                              | 省份地区	 | 信息类型	  | 采购人	         | 供应商	           | 中标金额	      |
|-----|-------------|----------------------------------|-------|--------|--------------|----------------|------------|
| 1   | 	2023-01-05 | 	邵阳市第一中学关于其他广告服务的网上超市采购项目成交公告    | 	湖南省  | 	中标结果  | 邵阳市第一中学      | 邵阳市双清区诚信广告传媒   | 42410.0元   |
| 2	  | 2022-08-06	 | 邵阳市第一中学老校区（邵阳市第十五中学）监控设备采购竞价成交公告 | 	湖南省  | 	中标结果	 | 邵阳市第一中学      | 湖南联诺智慧科技有限公司   | 274360.0元	 |
| 3	  | 2022-01-06	 | 邵阳市第一中学老校区（市十五中）云机房 采购项目	        | 湖南省	  | 招标公告	  | 邵阳市第一中学      | -              | -          |
| 4	  | 2017-12-06	 | 邵阳市住房公积金管理中心北塔区服务大厅办公用房单一来源采购公示	 | 湖南省	  | 招标公告   | 邵阳市住房公积金管理中心 | 邵阳市九盛房地产开发有限公司 | -          |

    """
)