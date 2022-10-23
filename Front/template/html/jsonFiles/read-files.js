// fetch('set1.json')
//   .then(function (response) {
//     return response.json();
//   })
//   .then(function(data) {
//     appendData(data);
//   }
//   .catch(function (err) {
//     console.log(err);
//   });

// function appendData(data) {
//   var mainContainer = document.getElementById("myData");
//   for (var i = 0; i < data.length; i++) {
//     var div = document.createElement("div");
//     div.innerHTML = 'Procedure: ' + data[i].proc_id;
//     mainContainer.appendChild(div);
//   }
// }

// let text = '{ "employees" : [' +
// '{ "firstName":"John" , "lastName":"Doe" },' +
// '{ "firstName":"Anna" , "lastName":"Smith" },' +
// '{ "firstName":"Peter" , "lastName":"Jones" } ]}';

const obj = JSON.parse(text);
