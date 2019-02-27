# reptile
python 爬虫学习总结

### xpath

* 基本语法
```text
/  从根节点选取
// 从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
. 代表选取当前阶段
.. 选择当前节点的浮点
@  选取属性

```
* 使用方式
```text
1.使用//获取整个页面的当前元素,然后在写谓词进行提取
 eg: //div[@class='abc']

2. xpath使用绝对路径(不推荐)
  语法://html/body/tag1[index]/tag2[index]/p/

3. xpath 属性定位
  语法: //htmltag[@attribute='value1' and @attribute2='value2']
      //input[contains(@id,'user')]
      //input[start-with(@name,'pass')]   //匹配第一个以pass开头的标签

4. xpath相对定位
  语法: //htmltag[@attribute='name']/htmltag/..../htmltag
  eg: //table[@id='value1']/tr[1]/td[3]/
```



