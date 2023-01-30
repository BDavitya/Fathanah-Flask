var z = document.getElementsByClassName("username");
for (var i = 0; i < z.length; i++) {
    let usrnm = document.getElementsByClassName("username")[i].value;
    a = usrnm.length
    b = a-1
    var d=[]
    d.push(usrnm[0])
    for (let i = 1; i < a; i++) {
        if(i == b){
            d.push(usrnm[i])
        }else{
            d.push('⋆');
        }
    }
    e = d.join(" ")
    let sensordata = document.getElementsByClassName("usernamee")[i]
    console.log(usrnm)
    sensordata.innerHTML=e
}