
// utils.js
module.exports = {
    range:  function(start, stop, step){
        let output = [];
        for (var i = start; i < stop; i += step){
           output.push(i);
        }
        return output;
     },
     compress: function(arr1, arr2){
        let output = [];
        for (const e of arr1.map( (e,i) => [e, arr2[i]]) ){
           if (e[1]) { output.push(e[0]) }
        }
        return output;
     }
}
 
