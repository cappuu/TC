
sub UNIT_ENTRY {

	&CHARA_MAIN_OPEN;
   	&COUNTRY_DATA_OPEN("$kcon");

	if($xcid eq "0"){&ERR("����λ�� ������ �� �����ϴ�.");}
	if($in{'unit_id'} eq "") { &ERR("�Ҽ��ϴ� �δ밡 ���õǾ� ���� �ʽ��ϴ�."); }

	open(IN,"$UNIT_LIST") or &ERR("������ ������ ������ �ʽ��ϴ�.");
	@UNI_DATA = <IN>;
	close(IN);

	@UNI_DATA2 = @UNI_DATA;

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

	foreach(@CL_DATA) {
	($aid,$apass,$aname,$achara,$astr,$aint,$alea,$acha,$asol,$agat,$acon,$agold,$arice,$acex,$aclass,$aarm,$abook,$abank,$asub1,$asub2,$apos,$ames,$ahost,$adate,$amail,$aos) = split(/<>/);
		if($in{'unit_id'} eq $aid){$jung = int($acha/8);}
	}

	$hit=0;
	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
		if($uid eq $kid){&ERR("�̹� $uunit_name �δ뿡 �Ҽ��� �ֽ��ϴ�.");}
	}

	$hit=0;
	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
		if($unit_id eq $in{'unit_id'}){last;}
	}

	$unit_num = 1;
	foreach(@UNI_DATA2){
	($unit_id2,$uunit_name2,$ucon2,$ureader2,$uid2,$uname2,$uchara2,$umes2,$uflg2)=split(/<>/);
		if("$unit_id" eq "$unit_id2" && !$ureader2){
		$unit_num++;
		}
	}

	if($jung < $unit_num){&ERR("�δ����� �ŷ�ġ�� �δ���� �޾Ƶ��̴µ� ���ڸ��ϴ�. [�δ��Ѱ谡�� : $jung��]");}

	if($uflg){
		&ERR("�Դ� �źΰ� �Ǿ����ϴ�.");
	}

	if(!$hit){
		unshift(@UNI_DATA,"$unit_id<>$uunit_name<>$kcon<>0<>$kid<>$kname<>$kchara<>$umes<>$uflg<>\n");
		open(IN,"$MESSAGE_LIST") or &ERR('������ ���� �ʾҽ��ϴ�.');
		@MES_REG = <IN>;
		close(IN);

		$mes_num = @MES_REG;

		if($mes_num > $MES_MAX) { pop(@MES_REG); }
		unshift(@MES_REG,"$unit_id<>$kid<>$kpos<>$kname<><font color=00FF00>���� : $kname���� $uunit_name �δ뿡 �Դ��߽��ϴ�.<>$uunit_name�δ�<>$daytime<>$kchara<>$kcon<>0<>\n");

		open(OUT,">$MESSAGE_LIST") or &ERR('������ ���� �ʾҽ��ϴ�.');
		print OUT @MES_REG;
		close(OUT);
	}

	open(OUT,">$UNIT_LIST") or &ERR('UNIT4 ���ο� �����͸� ������ �� �����ϴ�.');
	print OUT @UNI_DATA;
	close(OUT);

	&CHARA_MAIN_INPUT;

	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2>$uunit_name �δ뿡 �Դ��߽��ϴ�.</h2><p>

<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="�޴��� ���ƿ´�"></form></CENTER>
EOM
	&FOOTER;
	exit;
}
1;