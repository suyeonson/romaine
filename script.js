Parse.initialize("AkroJBS9kpJ8AL2bxcaMyNJrD6TmrKouEHWZrJGU", "jgyzkbCzZQYBJK63wZn9EWflKoxJWoh9BU9Vi5Pw");

window.fbAsyncInit = function() {
	Parse.FacebookUtils.init({
	appId      : '1569324956622321',
	status     : false,
	cookie     : true,
	xfbml      : true,
	version    : 'v2.1'
	});
};

(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&appId=1569324956622321&version=v2.0";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));