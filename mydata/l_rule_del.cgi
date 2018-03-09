
sub L_RULE_DEL{

	&CHARA_MAIN_OPEN;
	&TIME_DATA;
	&HOST_NAME;
	&COUNTRY_DATA_OPEN("$kcon");

	if($xcid eq "0"){&ERR("재야인사는 실행할 수 없습니다.");}
	if($in{'del_id'} eq "") { &ERR("메세지가 선택되지 않았습니다."); }
	if($xking ne $kid && $x0 ne $kid){&ERR("왕만이 법전을 삭제할 수 있습니다.");}

	if($lockkey) { &F_LOCK; }
	open(IN,"$LOCAL_LIST") or &ERR2('파일을 열지 않았습니다.err no :country');
	@LOCAL_DATA = <IN>;
	close(IN);

	$mhit=0;$hit=0;@NEW_LOCAL_DATA=();
	foreach(@LOCAL_DATA){
		($bbid,$bbno,$bbmes,$bbcharaimg,$bbname,$bbhost,$bbtime,$bbele,$bbcon,$bbtype)=split(/<>/);
		if("$bbno" eq "$in{'del_id'}"){
			$hit=1;
			$mes = "$bbmes";
		}else{
			push(@NEW_LOCAL_DATA,"$_");
		}
	}
	if(!$hit){&ERR("그 국법은 삭제할 수 없습니다.");}

	open(OUT,">$LOCAL_LIST") or &ERR('파일을 열지 않았습니다.');
	print OUT @NEW_LOCAL_DATA;
	close(OUT);

	if (-e $lockfile) { unlink($lockfile); }
	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2>$mes를 삭제했습니다.</h2><p>

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