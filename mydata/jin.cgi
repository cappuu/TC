sub JIN {

	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);
	&GWAN2;



	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR("���� ���� ����!");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);

	open(IN,"./charalog/main/$in{'id'}.cgi") or &ERR2('ID�� �н��� �ùٸ��� �ʽ��ϴ�!');
	@CN_DATA = <IN>;
	close(IN);

	($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$kskill,$kpoint,$kct) = split(/<>/,$CN_DATA[0]);
	($kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex) = split(/,/,$ksub1);

	&TIME_DATA;

	&HEADER;


	print <<"EOM";
	<form action="./mydata.cgi" method="post"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type="hidden" name="mode" value="JIN1">
	<input type="radio" name="jin" value="1">����1<br>
	<input type="radio" name="jin" value="2">����2<br>
	<input type="radio" name="jin" value="3">����3<br>
	<input type="radio" name="jin" value="4">����4<br>
	<input type="radio" name="jin" value="5">����5<br>
	<input type="submit" style="font-family:�ü�; color:rgb(255,153,0); background-color:rgb(41,60,66); border-style:none;" value="��������"></form>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="���ƿ´�"></form></CENTER>
</TD></TR></TABLE>
</TD></TR></TABLE>

EOM

	&FOOTER;

	exit;

}
1;

sub JIN1 {
	&CHARA_MAIN_OPEN;
	$jin_ex = $in{'jin'};
	$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
	&CHARA_MAIN_INPUT;

	if($in{'jin'} eq 1){
	$jinb = '����1';
	}elsif($in{'jin'} eq 2){
	$jinb = '����2';
	}elsif($in{'jin'} eq 3){
	$jinb = '����3';
	}elsif($in{'jin'} eq 4){
	$jinb = '����4';
	}elsif($in{'jin'} eq 5){
	$jinb = '����5';
	}

	&HEADER;
	print <<"EOM";
<center><h2><font color=blue>$jinb�� ������ �����Ͽ����ϴ�. $in{'jin'}</font></h2><hr size=0>
<br>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="Ȯ��"></form>
EOM

	&FOOTER;
	exit;
}