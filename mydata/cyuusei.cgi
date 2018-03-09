
sub CYUUSEI {

	if($in{'cyuu'} eq "") { &ERR("입력되지 않았습니다."); }
	if ($in{'cyuu'} =~ m/[^0-9]/){&ERR("숫자 이외의 문자가 포함되어 있습니다."); }
	if($in{'cyuu'} < 0 || $in{'cyuu'} > 100 ) { &ERR("0 ~ 100의 사이에 입력해 주십시오."); }


	$cyuu = $in{'cyuu'}+0;
	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kpos);

	&TIME_DATA;

	$kbank = $cyuu;
	$res_mes = "$kname님은 충성도를 $cyuu로 설정했습니다.";

	&CHARA_MAIN_INPUT;
	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>$res_mes</h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="확인"></form></CENTER>
EOM
	&FOOTER;

	exit;

}
1;