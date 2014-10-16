var params = {
	key: '',
	term: 4530,
	subject: 'SPANISH'
};

var courses;

$.getJSON('http://api.asg.northwestern.edu/courses/', params, function(data) {
  // data is the JavaScript array that results from parsing the response
  console.log(data);
  // console.log(data[0].id);
  var items = [];
  $.each( data, function(key, value) {
    items.push( "<li id='" + key + "'>" + data[key].subject + " " + data[key].catalog_num + ": " + data[key].title + "<br />" + data[key].instructor + "</li>" );
  });
 
  $( "<ul/>", {
  	"class": "my-new-list",
    html: items.join( "" )
  }).appendTo( "body" );
});