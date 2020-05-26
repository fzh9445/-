数据的抓取与清理
=
 数据的抓取
-

经过一番网页的分析之后发现只需抓取某些关键字段即可，如：出发日期、天数、人均消费、人物、玩法等，但由于某些网页的不规范原因，一些地名无法抓取，所以用攻略代替。部分代码如下图
![image](https://github.com/fzh9445/-/blob/master/%E5%9B%BE%E7%89%87/%E9%83%A8%E5%88%86%E4%BB%A3%E7%A0%81.png)

数据的清洗
-

将出发时间的改为标准时间，同时提取出旅游的月份单独作为一列；将人均消费100元以下的数据去除；浏览量同一规定格式为整形；天数99+数据去除。清除后数据如下图
![image](https://github.com/fzh9445/-/blob/master/%E5%9B%BE%E7%89%87/%E6%95%B0%E6%8D%AE%E5%9B%BE%E7%89%87.png)

评论词云分析
-
![image](https://github.com/fzh9445/-/blob/master/%E5%9B%BE%E7%89%87/%E8%AF%8D%E4%BA%91%E5%88%86%E6%9E%90.png)
‘攻略’、‘美食’、‘成都’、‘自驾’是权重最高的四个词，事实上我们去每个城市里旅游大多涉及到这四个方面。

旅游胜地前十推荐以及人均消费前十
-

![image](https://github.com/fzh9445/-/blob/master/%E5%9B%BE%E7%89%87/%E7%9B%AE%E7%9A%84%E5%9C%B0Top10.png)
![image](https://github.com/fzh9445/-/blob/master/%E5%9B%BE%E7%89%87/%E4%BA%BA%E5%9D%87%E6%B6%88%E8%B4%B9%E5%89%8D%E5%8D%81%E6%97%85%E6%B8%B8%E5%9C%B0.png)
成都以91的访问量稳居第一，成都的都江堰以及熊猫基地引客无数

出游天数
-

![image](https://github.com/fzh9445/-/blob/master/%E5%9B%BE%E7%89%87/%E6%97%85%E8%A1%8C%E6%97%B6%E9%95%BF.png)
旅游时长主要分布与2-4天，其中3太难占据绝大多数，3天刚刚好不太长也不太短个能够更好的领略城市风景

出游方式
-

![image](https://github.com/fzh9445/-/blob/master/%E5%9B%BE%E7%89%87/%E5%87%BA%E6%B8%B8%E7%BB%93%E4%BC%B4%E6%96%B9%E5%BC%8F.png)
三五好友占据比达41%

出游玩法
-

![image](https://github.com/fzh9445/-/blob/master/%E5%9B%BE%E7%89%87/%E5%87%BA%E6%B8%B8%E7%8E%A9%E6%B3%95.png)
‘摄影’、‘美食’、‘短途周末’，此三项稳居前三，一次完美的旅行离不开摄影和美食，而一次周末旅行也能放松一周工作所带来的疲惫。
