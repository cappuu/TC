
sub L_RULE_WRITE{

	&CHARA_MAIN_OPEN;
	&TIME_DATA;
	&HOST_NAME;
	&COUNTRY_DATA_OPEN("$kcon");

	if($xcid eq "0"){&ERR("재야인사는 실행할 수 없습니다.");}
	if(length($in{'title'}) > 40 || length($in{'ins'}) > 500) { &ERR("좀 더 간략하게 국법을 전해 주십시오."); }
	if($in{'ins'} eq "") { &ERR("메세지가 입력되어 있지 않습니다."); }

	open(IN,"$LOCAL_LIST") or &ERR2('파일을 열지 않았습니다. err no :country');
	@LOCAL_DATA = <IN>;
	close(IN);

	$bbs_num = @LOCAL_DATA;
	if($bbs_num > $MES_MAX) { pop(@LOCAL_DATA); }

	($bbid,$bbno)=split(/<>/,$LOCAL_DATA[0]);
	$s_no=$bbno+1;

	$numm = int($cex / $LANK);
	if($numm>20){$numm = 20;}
	$bbname = "$kname";
	if($in{"type"} eq "all"){$bbtype = 1;}else{$bbtype = 0;}
	unshift(@LOCAL_DATA,"$kid<>$s_no<>$in{'ins'}<>$kchara<>$bbname<>$host<>$daytime<>$kele<>$kcon<>$bbtype<>\n");

	open(OUT,">$LOCAL_LIST") or &ERR('파일을 열지 않았습니다.');
	print OUT @LOCAL_DATA;
	close(OUT);

	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2>법전을 제작했습니다.</h2><p>

<form action="$FILE_MYDATA" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=LOCAL_RULE>
<input type=submit value="확인"></form></CENTER>
EOM
	&FOOTER;
	exit;
	
}
1;