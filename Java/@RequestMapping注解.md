# @RequestMapping注解
在 Spring MVC 中使用 `@RequestMapping` 注解来实现 URL 路由映射，也就是浏览器连接程序的作用。
```
@Controller //让 spring 框架启动时，加载
@RequestMapping("/web") // 路由器规则注册
public class WebCOntroller 
    @ResponseBody // 返回⾮⻚⾯数据
    @RequestMapping("/indexData")
    public String indexData(){
        return "hello,spring mvc";
    }
}
```
@RequestMapping即是类注解，又是方法注解。访问的URL等于类注解+方法注解。　　
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/49b2c543-f228-4511-8712-ed3f352f6f7b)　　


### 指定 GET/POST 方法类型
**只支持GET请求的三种写法：**   
```
// 写法1
@RequestMapping("/indexData")
// 写法2
@RequestMapping(value = "/indexData",method = RequestMethod.GET)
// 写法3
@GetMapping("/indexData")
```  
**只支持POST请求的三种写法：** 
```
// 写法1
@RequestMapping("/indexData")
// 写法2
@RequestMapping(value = "/indexData",method = RequestMethod.POST)
// 写法3
@PostMapping("/indexData")
```  


### 获取参数
**获取单个参数**  
在 Spring MVC 中可以直接用方法中的参数来实现传参：  
```
@RestController
@RequestMapping("/para")
public class ParamController {
    @RequestMapping("/get2")
    public String get2(String name){
        return "name:" + name;
    }
}
```
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/bd53e29e-237b-43d8-915b-21b6442a771f)  
  

**获取多个参数**  
获取参数时，参数的顺序与url传参的参数顺序无关。并且进行了数据类型的转换。  
```
@RestController
@RequestMapping("/para")
public class ParamController {
    @RequestMapping("/get3")
    public String get3(String name,Integer age){
        return "name:" + name + "| age :" + age;
    }
}
```  
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/104a97af-35c1-479d-b496-691b09e71689)  


**传递对象**  
如果参数非常多，一个一个写也不现实，而且参数这个会使得耦合度太高。此时需要将参数封装成一个对象。Spring MVC 可以⾃动实现参数对象的赋值，比如 Student 对象:  
```
@Data
public class Student {
    private Integer id;
    private String name;
    private Integer age;
}

@RestController
@RequestMapping("/para")
public class ParamController {
    @RequestMapping("/get6")
    public String get6(Student student){
        return student.toString();
    }
}

```
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/3ad3d021-1e75-44e1-bfd2-3eefb7cf5096)  


**表单参数的传递**  
这是前端传递参数的方式，与接收参数的方式无关。ajax，form表单，浏览器传参等各种方式都可以。  
当有多个参数时，前后端进⾏参数匹配时，是以参数的名称进⾏匹配的，因此参数的位置是不影响后端获取参数的结果。  
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/cde8169a-a4b4-4149-bbc2-191d54996115)    


**后端参数重命名**  
某些特殊的情况下，前端传递的参数 key 和我们后端接收的 key 可以不⼀致，比如前端传递了⼀个n 给后端，而后端又是有 name 字段来接收的，这样就会出现参数接收不到的情况，如果出现这种情况，我们就可以使用 `@RequestParam `来重命名前后端的参数值。  
```
@RestController
@RequestMapping("/para")
public class ParamController {

    @RequestMapping("/get7")
    public String get7(@RequestParam("n") String name){
        return "name :" + name;
    }
}

```   
把调用方发送的参数n，重命名为name。  
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/140ba8a2-ea66-4bcc-85c0-ff6fc67f9813)  


**必传参数与非必传参数**  
如果实际业务前端的参数是⼀个非必传的参数，我们可以通过设置 @RequestParam 中的required=false 来避免步传递时报错.  
```
@RestController
@RequestMapping("/para")
public class ParamController {
    @RequestMapping("/get7")
    public String get7(@RequestParam(value = "n",required = false) String name){
        return "name :" + name;
    }
}

```
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/9ea078d8-b88c-4306-b490-21dacfdc5edc)  


**其他的可以参考这里**  
https://blog.csdn.net/qq_43243800/article/details/132010781  
























