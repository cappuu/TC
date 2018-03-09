
sub IVEN {

	&CHARA_MAIN_OPEN;

	open(IN,"$ARM_LIST");
	@ARM_DATA = <IN>;
	close(IN);
	foreach(@ARM_DATA){
	($armname,$armval,$armdmg,$armwei,$armele,$armsta,$armclass,$armtownid)=split(/<>/);
	}

	open(IN,"./logfile/item/$kid.cgi");
	@ITEM = <IN>;
	close(IN);
	$no2=0;
	foreach(@ITEM){
		($itemname,$itemval,$itemdmg,$itemwei,$itemele,$itemmsta,$itemclass,$itemtownid) =split(/<>/);
		$mok .= print qq|$itemname\n|;
	}

	&HEADER;

	print <<"EOM";
<html>
<body>
아이템목록:$mok
</body>
</html>
EOM

	&FOOTER;
	exit;
}
1;