var a={"a1":123,"a2":1234};
var b=["a",1,"b",2];
b.forEach(function(element,index) {  
    console.log('element,i :',element,index);
});
    
for(var i in a){
    console.log('a :', a[i],i);
}

console.log('a :', a);
console.log('a :', a);