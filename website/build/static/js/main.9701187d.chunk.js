(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{121:function(e,a,t){e.exports=t(290)},126:function(e,a,t){},288:function(e,a,t){},290:function(e,a,t){"use strict";t.r(a);var n=t(1),l=t.n(n),r=t(52),i=t.n(r),s=(t(126),t(109)),c=t(110),o=t(240),m=t(111),u=t(241),d=t(294),h=t(295),E=t(292),p=t(231),w=t(230),v=t(291);var f=function(e){var a=e.user,t=a.data_points,n=a.insta&&a.insta.length>0,r=t&&t.length>0;return l.a.createElement("div",{className:"user-view"},l.a.createElement("div",{className:"user-info"},l.a.createElement("div",{className:"user-image"},l.a.createElement("img",{src:a.image_url})),l.a.createElement("div",{className:"user-name"},l.a.createElement("p",null,a.name),n&&l.a.createElement("p",{className:"user-handle"},l.a.createElement("a",{href:"https://www.instagram.com/"+a.insta+"/"},"@"+a.insta)))),r&&l.a.createElement("div",{className:"follower-count"},l.a.createElement("span",null,"Followers: "),l.a.createElement("span",null,t[t.length-1].num_followers)),a.delta&&l.a.createElement("div",{className:"follower-delta"},a.delta>0&&l.a.createElement("div",{className:"up"},l.a.createElement("span",null,"Up"),l.a.createElement("span",null,a.delta)),a.delta<0&&l.a.createElement("div",{className:"down"},l.a.createElement("span",null,"Down"),l.a.createElement("span",null,a.delta))),r&&l.a.createElement("div",{className:"chart-view"},l.a.createElement(d.a,{width:"100%",height:250},l.a.createElement(h.a,{data:t,margin:{top:5,right:5,bottom:5,left:5}},l.a.createElement(E.a,{type:"monotone",dataKey:"num_followers",stroke:"#8884d8"}),l.a.createElement(p.a,{type:"number",domain:["dataMin","dataMax"],orientation:"right",axisLine:!1,tickLine:!1,hide:!0}),l.a.createElement(w.a,{dataKey:"timestamp",padding:{right:30},axisLine:!1,tickLine:!1,hide:!0}),l.a.createElement(v.a,null)))))},g=t(120),k=t.n(g),y=t(232);t(288);y.a.initialize("UA-131786508-1");var N=function(e){function a(){return Object(s.a)(this,a),Object(o.a)(this,Object(m.a)(a).apply(this,arguments))}return Object(u.a)(a,e),Object(c.a)(a,[{key:"componentDidMount",value:function(){this.setState({users:[]}),this.loadData("week")()}},{key:"loadData",value:function(e){var a=this;return function(){k.a.get("http://localhost:5000/update/?filter="+e).then(function(e){a.setState({users:e.data})})}}},{key:"render",value:function(){y.a.pageview("/homepage");var e=[];return this.state&&(e=this.state.users),l.a.createElement("div",{className:"App"},l.a.createElement("h1",null,"Bachelor Insta Followers"),l.a.createElement("div",{className:"date-selector"},l.a.createElement("a",{onClick:this.loadData("day")},"Day"),l.a.createElement("a",{onClick:this.loadData("week")},"Week"),l.a.createElement("a",{onClick:this.loadData("month")},"Month")),l.a.createElement("div",{className:"user-container"},e.map(function(e,a){return l.a.createElement(f,{user:e,key:a})})))}}]),a}(n.Component);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));i.a.render(l.a.createElement(N,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then(function(e){e.unregister()})}},[[121,2,1]]]);
//# sourceMappingURL=main.9701187d.chunk.js.map