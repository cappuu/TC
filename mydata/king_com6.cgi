sub KING_COM6 {

	if($in{'sel'} eq ""){&ERR("임명 상대가 입력되지 않았습니다.");}
	if($in{'type'} eq ""){&ERR("대상이 입력되지 않았습니다.");}
	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN("$kcon");
	&TIME_DATA;

	open(IN,"./charalog/main/$in{'sel'}.cgi") || &ERR("그 ID는 존재하지 않습니다.");
	@E_DATA = <IN>;
	close(IN);


	($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/,$E_DATA[0]);

	if($x0 eq $eid){$x0 = "";}elsif($x1 eq $eid){$x1="";}elsif($x2 eq $eid){$x2="";}elsif($x3 eq $eid){$x3="";}elsif($x4 eq $eid){$x4="";}elsif($x5 eq $eid){$x5="";}elsif($x6 eq $eid){$x6="";}elsif($x7 eq $eid){$x7="";}elsif($x8 eq $eid){$x8="";}elsif($x9 eq $eid){$x9="";}elsif($x10 eq $eid){$x10="";}elsif($x11 eq $eid){$x11="";}elsif($x12 eq $eid){$x12="";}elsif($x13 eq $eid){$x13="";}elsif($x14 eq $eid){$x14="";}elsif($x15 eq $eid){$x15="";}elsif($x16 eq $eid){$x16="";}elsif($x17 eq $eid){$x17="";}elsif($x18 eq $eid){$x18="";}elsif($x19 eq $eid){$x19="";}elsif($x20 eq $eid){$x20="";}
	elsif($x21 eq $eid){$x21="";}elsif($x22 eq $eid){$x22="";}elsif($x23 eq $eid){$x23="";}elsif($x24 eq $eid){$x24="";}elsif($x25 eq $eid){$x25="";}elsif($x26 eq $eid){$x26="";}else{&ERR("해당장수는 아무 관직도 임명되지 않았습니다.");}

	$xsub = "$x0,$x1,$x2,$x3,$x4,$x5,$x6,$x7,$x8,$x9,$x10,$x11,$x12,$x13,$x14,$x15,$x16,$x17,$x18,$x19,$x20,$x21,$x22,$x23,$x24,$x25,$x26,$xxsub1,$xxsub2,";

	&COUNTRY_DATA_INPUT;
	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>$ename를 해임했습니다.</h2><p>
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