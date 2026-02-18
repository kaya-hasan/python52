//import { topla, cikar, PI } from "./moduller.js";

//console.log(topla(55, 66));
//console.log(cikar(99, 66));
//console.log(PI);

// as ile çağırılan fonksiyonlar için yeni isimler verilebilir
import { topla as add, cikar as minus } from "./moduller.js";
console.log(add(55, 66));
console.log(minus(99, 66));

// Toplu import özelliği
import * as matematik from "./moduller.js";
console.log(matematik.topla(10, 20));
console.log(matematik.cikar(50, 30));
