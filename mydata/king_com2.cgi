
sub KING_COM2 {

	if($in{'mes'} eq ""){&ERR("지령이 입력되지 않았습니다.");}
	if(length($in{'mes'}) > 100) { &ERR("편지는 전각 50 문자 이하로 입력해 주세요."); }
	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);

	if($xking ne $kid && $x0 ne $kid){&ERR("왕이나 참모가 아니면 실행할 수 없습니다.");}

	if($xking eq $kid){
		$add = "군주";
	}elsif($x0 eq $kid){
		$add = "참모";
	}

	$xmes = "$in{'mes'}($add $kname印)";
	&COUNTRY_DATA_INPUT;

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>지령을 입력했습니다.</h2><p>
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