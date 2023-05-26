# 开始react
创建完react项目后，删除掉src文件下所有文件，并在里面创建一个index.js文件，react会自动将它作为项目的入口。  
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/c334ab6d-f696-419f-803c-ae9c303210bc) 
这下面两个包是react项目必须引入的。  
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/b9e9b857-ec33-40b0-a556-3b20116982e9)   
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/2cf84ee7-15b8-4754-bd50-4017c9b9d89c)   


# 类组件
自定义的 React 类名必须以大写字母开头。  
`ReactDOM.render` 是 React 的最基本方法用于将模板转为 HTML 语言，并插入指定的 DOM 节点。  
`ReactDOM.render(template,targetDOM)`方法接收两个参数：  
 第一个是创建的模板，多个 dom 元素外层需使用一个标签进行包裹，如 <div>，并且标签中间不能有空行断开；  
 第二个参数是插入该模板的目标位置。  
若要为创建的某个元素增加 class 属性，不能直接定义 class 而要用 className，因为 class 是 javascript 中的保留字,同样可以定义行内样式，将所有的样式包裹在一个对象中，以类似变量的形式给 style 属性赋值，注意样式属性要用驼峰命名法表示，如: backgroundColor 而不是 background-color，fontSize 而不是 font-size。      
```
  # 例如：
  <input type="text"  className="userName" style={{"backgroundColor":"yellow","color":"red"}} value={value}/> 
  # 外界传入的变量一个{}即可， 写死的变量用两个{{ }}来写。
``` 
**模板**
```
  # extends React.Component 必须继承这个类 否则App就是个普通的自定义类
  class App extends React.Component{
    # 必须用render(){}方法来返回，否则标签渲染不出来。  
    render(){
        return <div>hello react</div>
    }
}
# 用export来将这个组件导出
export default App
```
  
  
# 函数组件  
要求跟类组件一样，只是不用继承React.Component了。  
```
  function App(){
    return <div>
        hello react
    </div>
}

export default App
```  
  
 # 组件的嵌套
 ```
import React, { Component } from 'react'

function Function_1(){
    return <div>function_1</div>
}

const Function_2 = () => {
    return <div>Function_2</div>
}

class Class_2 extends Component {
    render(){
        return <div>Class_2</div>
    }
}

class Class_1 extends Component {
    render(){
        return <div>
                Class_1
                # 子组件中还可以定义子组件
                <Class_2></Class_2>
            </div>
    }
}

export default class App extends Component {
  render() {
    return (
      <div className='active'>
       # 将定义好的组件当作标签写入即可
            <Function_1></Function_1>
            <Function_2></Function_2>
            <Class_1></Class_1>
            标签当中可以加上大括号放入表达式，但是不能放入if，while等语句。
            {10 + 20}
      </div>
    )
  }
}
 ```
 
 
 # 引入样式
 在外部定义好样式内容。  
 ![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/4fd816c6-1ed3-49e3-a873-ab1e3b4d9da0)   
在想要引入样式的地方加上对应的类名。    
 ![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/722f2486-49a5-4405-8844-9422b5a7ffab)   
然后引入对应的样式文件并渲染即可。    
 ![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/1f2d5229-c5ab-4336-8a84-38dcbd840f5a)    

 
# 事件绑定
react是声明式的，不用像js那样捕获节点，添加处理函数。  
把事件的js文件写好，并向之前那样在index.js当中被引入渲染即可。 
react当中事件都是on + 事件名的形式，后面等号就是要触发的函数
```
import React, { Component } from 'react'

export default class Event extends Component {
  render() {
    return (
      <div>
        event
        <input/>
        <button onClick={() => {
            console.log('onClick')
        }}>onClick_1</button>

        <button onClick={() => {
            this.handleClick()
        }}>onClick_2</button>

      </div>
    )
  }

  handleClick(){
    console.log('handleClick')
  }

}
```  
 
 
 
 
