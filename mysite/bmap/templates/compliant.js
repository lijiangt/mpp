var currentTab;function showTab(strID,objTrigger){var objTab=document.getElementById(strID);if(objTab){show(strID);if(currentTab&&(currentTab!=objTab)){hide(currentTab.id);currentTab.style.display="none";}}
currentTab=objTab;var objTabs=document.getElementById("tabs");var arrTabs=objTabs.getElementsByTagName("li");if(objTrigger){for(var i=0;i<arrTabs.length;i++){arrTabs[i].className="";}
var objTriggerTab=objTrigger.parentNode;if(objTriggerTab){objTriggerTab.className="active";}}
var e=document.createEvent('HTMLEvents');e.initEvent('resize',true,true);window.dispatchEvent(e);onDOMChange();}
function rotateScreen(){switch(window.orientation){case 0:case 180:setOrientation('portrait');break;case-90:case 90:setOrientation('landscape');break;default:setOrientation('portrait');break;}
setTimeout(scrollToTop,500);}
function setOrientation(orientation){document.getElementsByTagName("body")[0].className=orientation;}
function showLoadingMsg(strID){var objToStuff=document.getElementById(strID);if(objToStuff){objToStuff.style.height=objToStuff.offsetHeight+"px";objToStuff.innerHTML="<div class=\"loading\"><img src=\"../Webkit/images/loading.gif\" width=\"27\" height=\"21\" alt=\"\" align=\"absmiddle\" />Loading data...</div >";}
onDOMChange();}
function hide(strID){var objToHide=document.getElementById(strID);if(objToHide){objToHide.style.display="none";}
onDOMChange();}
function show(strID){var objToHide=document.getElementById(strID);if(objToHide){objToHide.style.display="block";}
onDOMChange();}
function showHideFull(objContainer){var strClass=objContainer.className;if(strClass.indexOf("collapsed")>-1){strClass=strClass.replace("collapsed","expanded");}else{strClass=strClass.replace("expanded","collapsed");}
objContainer.className=strClass;objContainer.blur();onDOMChange();}
function clearField(objField,strDefault){if((objField.value==strDefault)||(objField.value=="")){objField.value="";}}
function androidPlaceholderFix(searchbox){if(searchbox.value==""){searchbox.value="";}}
function getCookie(name){var cookie=document.cookie;var result="";var start=cookie.indexOf(name+"=");if(start>-1){start+=name.length+1;var end=cookie.indexOf(";",start);if(end<0){end=cookie.length;}
result=unescape(cookie.substring(start,end));}
return result;}
function setCookie(name,value,expireseconds,path){var exdate=new Date();exdate.setTime(exdate.getTime()+(expireseconds*1000));var exdateclause=(expireseconds==0)?"":"; expires="+exdate.toGMTString();var pathclause=(path==null)?"":"; path="+path;document.cookie=name+"="+value+exdateclause+pathclause;}
function getCookieArrayValue(name){var value=getCookie(name);if(value&&value.length){return value.split(',');}else{return new Array();}}
function setCookieArrayValue(name,values,expireseconds,path){var value='';if(values&&values.length){value=values.join(',');}
setCookie(name,value,expireseconds,path);}
function hasClass(ele,cls){return ele.className.match(new RegExp('(\\s|^)'+cls+'(\\s|$)'));}
function addClass(ele,cls){if(!this.hasClass(ele,cls))ele.className+=" "+cls;}
function removeClass(ele,cls){if(hasClass(ele,cls)){var reg=new RegExp('(\\s|^)'+cls+'(\\s|$)');ele.className=ele.className.replace(reg,' ');}}
function toggleClass(ele,cls){if(hasClass(ele,cls)){removeClass(ele,cls);}else{addClass(ele,cls);}}
function showShare(){document.getElementById("sharesheet").style.display="block";document.addEventListener('touchmove',doNotScroll,true);}
function hideShare(){document.getElementById("sharesheet").style.display="none";document.removeEventListener('touchmove',doNotScroll,true);}
function doNotScroll(event){event.preventDefault();event.stopPropagation();}
function setBookmarkStates(name,item){var bookmark=document.getElementById("bookmark");var items=getCookieArrayValue(name);for(var i=0;i<items.length;i++){if(items[i]==item){addClass(bookmark,"on");break;}}
bookmark.addEventListener("touchstart",function(){addClass(bookmark,"pressed");},false);bookmark.addEventListener("touchend",function(){removeClass(bookmark,"pressed");},false);}
function toggleBookmark(name,item,expireseconds,path){var bookmark=document.getElementById("bookmark");toggleClass(bookmark,"on");var items=getCookieArrayValue(name);var newItems=new Array();if(items.length==0){newItems[0]=item;}else{var found=false;for(var i=0;i<items.length;i++){if(items[i]==item){found=true;}else{newItems.push(items[i]);}}
if(!found){newItems.push(item);}}
setCookieArrayValue(name,newItems,expireseconds,path);};function scrollToTop(){scrollTo(0,1);}
function onDOMChange(){};function setupNewsListing(){var newsEllipsizer=new ellipsizer();for(var i=0;i<100;i++){var elem=document.getElementById('ellipsis_'+i);if(!elem){break;}
newsEllipsizer.addElement(elem);}};function loadSection(select){window.location="./?section="+select.value;}
function toggleSearch(){var categorySwitcher=document.getElementById("category-switcher");if(categorySwitcher.className=="search-mode"){categorySwitcher.className="category-mode";}else{categorySwitcher.className="search-mode";document.getElementById("search_terms").focus();}
return false;}
function submitenter(myfield,e){var keycode;if(window.event){keycode=window.event.keyCode;}else if(e){keycode=e.keyCode;}else{return true;}
if(keycode==13){myfield.form.submit();return false;}else{return true;}}