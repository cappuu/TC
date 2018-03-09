#!/usr/bin/perl

print "Content-type: text/html\n\n";
print<<"HTMLTAG";
<title>삼국지 모의전투 NET - 칠랑서버</title>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN">
	<html>
	<head>
	<LINK REL="SHORTCUT ICON" href="samgug.ico">  
	<title>$TITLE</title>
	<frameset rows="99%,1" frameborder=0 border=0 framespacing=0>
		<frame src="/sam/dkajlfjeioaefhoiwqhfeouihwefwefksdjklfjwe.cgi" name="Main">
		<frame noresize src="/sam/music.html" scrolling="no" name="Sub">
	</frameset>
	</head>
	</html>
HTMLTAG
exit;