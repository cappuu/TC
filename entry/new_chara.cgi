sub NEW_CHARA {



	open(IN,"$member_list") or &ERR2('������ ���� �ʾҽ��ϴ�. err no :country');
	@MEMBER_DATA = <IN>;
	close(IN);

	foreach(@MEMBER_DATA){
		($mname,$mpass)=split(/<>/);
		if($mname eq "$hi[$in{'chara'}]"){
		if($mpass eq "$in{'pass'}"){
		}else{
		&E_ERR("��$mname���̶� ������� Ư�� �����̹Ƿ� ����� �� �����ϴ�.");
		}
		}
	}

	&CHEACKER;
	if($CHARA_STOP){ &ERR2("���� �ű� ����� �޾Ƶ����� �ʰ� �ֽ��ϴ�."); }
	if ($in{'license'} eq "") {&E_ERR("ĥ�������� �̿����� �������� �ʾҽ��ϴ�."); }
	if ($in{'id'} =~ m/[^0-9a-zA-Z]/) {&E_ERR("ID�� �ݰݿ����� �̿��� ���ڰ� ���ԵǾ� �ֽ��ϴ�."); }
	if ($in{'pass'} =~ m/[^0-9a-zA-Z]/) {&E_ERR("�н����忡 �ݰݿ����� �̿��� ���ڰ� ���ԵǾ� �ֽ��ϴ�."); }
	if ($in{'mail'} eq "" || $in{'mail'} !~ /(.*)\@(.*)\.(.*)/){&E_ERR("������ �Է��� �ùٸ��� �ʽ��ϴ�.");}
	if($in{'id'} eq "" or length($in{'id'}) < 4 or length($in{'id'}) > 8) { &E_ERR("ID��, 4���� �̻� 8���� ���Ϸ� �Է��ϱ� �ٶ��ϴ�."); }
	elsif($in{'pass'} eq "" || length($in{'pass'}) < 4 || length($in{'pass'}) > 8) { &E_ERR("�н������ 4���� �̻� 8���� ���Ϸ� �Է��ϱ� �ٶ��ϴ�."); }
	elsif($in{'con'} eq "") { &E_ERR("�ʱ� ��ġ�� ���õ��� �ʾҽ��ϴ�."); }
	elsif($in{'mail'} eq "\@" || $in{'mail'} eq "") { &E_ERR("������ �Է��� �ùٸ��� �ʽ��ϴ�."); }
	elsif($in{'pass'} eq "" || length($in{'pass'}) < 4 || length($in{'pass'}) > 16) { &E_ERR("ĳ������ �н����尡 �ùٸ��� �Էµ��� �ʾҽ��ϴ�."); }
	elsif($in{'id'} eq $in{'pass'}){&E_ERR("ID�� �н����尡 ���� ���, ����� �� �����ϴ�."); }
	elsif($in{'type'} eq "") { &E_ERR("��� Ÿ���� ���õ��� �ʾҽ��ϴ�."); }

	if ($in{'chara'} =~ m/[^0-9]/){&E_ERR("�ùٸ��� �ʽ��ϴ�."); }


	if($in{'cou_name1'} eq "1"){
		$in{'cou_name'} = "��";
		$in{'ele'} = "1";
	}elsif($in{'cou_name1'} eq "2"){
		$in{'cou_name'} = "��";
		$in{'ele'} = "2";
	}elsif($in{'cou_name1'} eq "3"){
		$in{'cou_name'} = "��";
		$in{'ele'} = "3";
	}elsif($in{'cou_name1'} eq "4"){
		$in{'cou_name'} = "��";
		$in{'ele'} = "4";
	}elsif($in{'cou_name1'} eq "5"){
		$in{'cou_name'} = "��";
		$in{'ele'} = "5";
	}elsif($in{'cou_name1'} eq "6"){
		$in{'cou_name'} = "��";
		$in{'ele'} = "6";
	}elsif($in{'cou_name1'} eq "7"){
		$in{'cou_name'} = "����";
		$in{'ele'} = "7";
	}elsif($in{'cou_name1'} eq "8"){
		$in{'cou_name'} = "�Ŷ�";
		$in{'ele'} = "8";
	}elsif($in{'cou_name1'} eq "9"){
		$in{'cou_name'} = "����";
		$in{'ele'} = "9";
	}

	open(IN,"$COUNTRY_LIST") or &ERR2('������ ���� �ʾҽ��ϴ�. err no :country');
	@COU_DATA = <IN>;
	close(IN);

	foreach(@COU_DATA){
		($xxcid,$xxname,$xxele,$xxnum,$xxins,$xxind,$xxall,$xxgold,$xxhp,$xxmaxhp,$xxstr,$xxvit,$xxagi)=split(/<>/);
	if($xxname eq $in{'cou_name'}){&E_ERR("�� ����� �̹� �����մϴ�.");}
	}

	$st[0] = 10;
	$st[1] = 10;
	$st[2] = 10;
	$st[3] = 10;

	for($i=0;$i<100;$i++){
		$st[int(rand(4))]++;
	}
	for($i=0;$i<4;$i++){
		$st[int(rand(4))]+=5;
	}

	if($in{'type'} eq "1"){
		$st[int(rand(4))]+=20;
		$st[int(rand(4))]+=10;
		$st[0]+=5;
		$st[1]+=5;
		if( $st[0] > $st[2] ){
			$in{'str'} = $st[0];
			$in{'int'} = $st[2];
		}else{
			$in{'str'} = $st[2];
			$in{'int'} = $st[0];
		}
		if( $st[1] > $st[3] ){
			$in{'tou'} = $st[1];
			$in{'cha'} = $st[3];
		}else{
			$in{'tou'} = $st[3];
			$in{'cha'} = $st[1];
		}
	}elsif($in{'type'} eq "2"){
		$st[int(rand(4))]+=20;
		$st[int(rand(4))]+=10;
		$st[0]+=5;
		$st[1]+=5;
		if( $st[0] < $st[2] ){
			$in{'str'} = $st[0];
			$in{'int'} = $st[2];
		}else{
			$in{'str'} = $st[2];
			$in{'int'} = $st[0];
		}
		if( $st[1] < $st[3] ){
			$in{'tou'} = $st[1];
			$in{'cha'} = $st[3];
		}else{
			$in{'tou'} = $st[3];
			$in{'cha'} = $st[1];
		}
	}else{
		$st[int(rand(4))]+=10;
		$st[int(rand(4))]+=10;
		$st[int(rand(4))]+=10;
		$st[int(rand(4))]+=10;
		$in{'str'} = $st[0];
		$in{'int'} = $st[1];
		$in{'tou'} = $st[2];
		$in{'cha'} = $st[3];
	}
	$max = $in{'str'} + $in{'int'} + $in{'tou'} + $in{'cha'};
	if($max ne "200"){
		&E_ERR("�հ��� �ɷ��� 200�� �ƴմϴ�. (�հ� $max)");
	}

	open(IN,"$TOWN_LIST") or &E_ERR("������ ������ ������ �ʽ��ϴ�.");
	@TOWN_DATA = <IN>;
	close(IN);

	open(IN,"$COUNTRY_LIST") or &E_ERR('������ ���� �ʾҽ��ϴ�. err no :country');
	@COU_DATA = <IN>;
	close(IN);

	open(IN,"$COUNTRY_NO_LIST") or &E_ERR('������ ���� �ʾҽ��ϴ�. err no :country no');
	@COU_NO_DATA = <IN>;
	close(IN);

	$zc=0;$m_hit=0;
	
	($z2name,$z2con)=split(/<>/,$TOWN_DATA[$in{'con'}]);
	if($z2con eq "" && $in{'gunju'} eq 1){
		if($in{'ele'} eq ""){
			&E_ERR("������ ���� ���� �������ּ���.");
		}elsif($in{'cou_name'} eq "" || length($in{'cou_name'}) < 2 || length($in{'cou_name'}) > 8) { &E_ERR("������ �̸��� �ùٸ��� �Էµ��� �ʾҽ��ϴ�."); }
		$m_hit = 1;
		$cou_name = $in{'cou_name'};
		$new_cou_no = @COU_NO_DATA + 1;
		$hit = 1;
	}else{
		foreach(@COU_DATA){
			($xcid,$xname,$xele,$xmark,$xking,$xmes,$xsub,$xpri)=split(/<>/);
			if($xcid eq $z2con){
				$cou_name = $xname;
				$kcon = $xcid;
				$hit = 1;
			}
		}
	}


	if($lockkey) { &F_LOCK; }

	&SET_COOKIE;
	&HOST_NAME;

	$date = time();
	$pos = 2;
	open(IN,"./charalog/main/$in{'id'}.cgi");
	@NEWCHARA = <IN>;
	close(IN);

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&E_ERR("���� ���� ����!");
			}
			@page = <page>;
			close(page);
			push(@REGIST_VI,"@page<br>");
		}
	}
	closedir(dirlist);


	$hit=0;@new_chara=();
	($rkid,$rkpass,$rkname,$rkchara,$rkstr,$rkint,$rklea,$rkcha,$rksol,$rkgat,$rkcon,$rkgold,$rkrice,$rkcex,$rkclass,$rkarm,$rkbook,$rkbank,$rksub1,$rksub2,$rkpos,$rkmes,$rkhost,$rkdate,$rkmail,$rkos,$rkskill,$rkpoint,$rkct,$rklevel,$rkexp,$rkcodea,$rkcodeb,$rkqpoint) = split(/<>/,$NEWCHARA[0]);


	foreach(@REGIST_VI){
		($rkid,$rkpass,$rkname,$rkchara,$rkstr,$rkint,$rklea,$rkcha,$rksol,$rkgat,$rkcon,$rkgold,$rkrice,$rkcex,$rkclass,$rkarm,$rkbook,$rkbank,$rksub1,$rksub2,$rkpos,$rkmes,$rkhost,$rkdate,$rkmail,$rkos,$rkskill,$rkpoint,$rkct,$rklevel,$rkexp,$rkcodea,$rkcodeb,$rkqpoint) = split(/<>/);
		if($ACCESS){
			if($host eq $rkhost ){
				&E_ERR("�� �� ���� �� ĳ�����Դϴ�. Ȥ�� ���� �����ǰ� �̹� ��ϵǾ� �ֽ��ϴ�.");
			}
		}
		if($rkmail eq "$in{'mail'}"){
			&E_ERR("�� ���� �ּҴ� �̹� ��ϵǾ� �ֽ��ϴ�.");
		}
		if($rkchara eq "$in{'chara'}"){
			
			&E_ERR("�̹� �� ������� �������� ����ϰ� �ֽ��ϴ�.");
		}
		if($kcon eq $rkcon){
			$con_num++;
		}
	}

	if($m_hit){
		$kcon = $new_cou_no;

		$month_read = "./log_file/date_count.cgi";
		open(IN,"$month_read") or &E_ERR('������ ���� �ʾҽ��ϴ�.');
		@MONTH_DATA = <IN>;
		close(IN);
		($myear,$mmonth,$mtime) = split(/<>/,$MONTH_DATA[0]);
		$old_date = sprintf("%02d\��%02d\��", $F_YEAR+$myear, $mmonth);

		push(@COU_DATA,"$new_cou_no<>$in{'cou_name'}<>$in{'ele'}<>1<>$in{'id'}<><>$hi[$in{'chara'}]<>1<><>\n");
		open(OUT,">$COUNTRY_LIST") or &E_ERR('COUNTRY �����͸� ������ �� �����ϴ�.');
		print OUT @COU_DATA;
		close(OUT);

		push(@COU_NO_DATA,"$new_cou_no<>$in{'cou_name'}<>$in{'ele'}<>1<>$in{'id'}<><><>1<><>\n");
		open(OUT,">$COUNTRY_NO_LIST") or &E_ERR('COUNTRY �����͸� ������ �� �����ϴ�.');
		print OUT @COU_NO_DATA;
		close(OUT);

		&TOWN_DATA_OPEN("$in{'con'}");
		$zcon = $new_cou_no;
		&TOWN_DATA_INPUT;
		&MAP_LOG2("<img src=$IMG/j13.gif> [$old_date\] $hi[$in{'chara'}], $cou_name���� �Ǳ��ϴ�.");
		&MAP_LOG("<img src=$IMG/j13.gif> [$old_date\] $hi[$in{'chara'}], $cou_name���� �Ǳ��ϴ�.");

	}else{
		&MAP_LOG("<img src=$IMG/b18.gif> $hi[$in{'chara'}]���� ���л�Ȱ�� ��� ������ �پ������ϴ�.");
	}

	@NEW_COM=();
	for($i=0;$i<$MAX_COM;$i++){
		push(@NEW_COM,"<><><>$tt<><><>50<>\n");
	}

	open(OUT,">./charalog/command/$in{'id'}.cgi");
	print OUT @NEW_COM;
	close(OUT);

	@NEW_COM1=();
	for($i=0;$i<30;$i++){
		push(@NEW_COM1,"�Ϲݰ���<>1<>0<>0<>\n");
	}

	open(OUT,">./charalog/command1/$in{'id'}.cgi");
	print OUT @NEW_COM1;
	close(OUT);

	@NEW_HIS=();

	open(OUT,">./charalog/history/$in{'id'}.cgi");
	print OUT @NEW_HIS;
	close(OUT);

	if($ATTESTATION){
		&mail_to;
		$os = 0;
	}else{
		$os = 1;
	}

	$ksol = 0;
	$kgat = 0;
	$kgold = 1000;
	$krice = 500;
	$kcex = 0;
	$kclass = 0;
	$karm = 0;
	$kbook = 0;
	$kbank = "16";
	$ksub1 = "";
	$ksub2 = $DEL_TURN - 10;
	$kstr = $in{'str'}+0;
	$kint = $in{'int'}+0;
	$ktou = $in{'tou'}+0;
	$kcha = $in{'cha'}+0;

	if($m_hit){
	unshift(@new_chara,"$in{'id'}<>$in{'pass'}<>$hi[$in{'chara'}]<>$in{'chara'}<>$kstr<>$kint<>$ktou<>$kcha<>$ksol<>$kgat<>$kcon<>$kgold<>$krice<>$kcex<>$kclass<>$karm<>$kbook<>$kbank<>$ksub1<>$ksub2<>$in{'con'}<>$in{'mes'}<>$host<>$date<>$in{'mail'}<>1<><>0<>$in{'con'}<>1<>0<><>A0<>0<>\n");
	}else{
	unshift(@new_chara,"$in{'id'}<>$in{'pass'}<>$hi[$in{'chara'}]<>$in{'chara'}<>$kstr<>$kint<>$ktou<>$kcha<>$ksol<>$kgat<><>$kgold<>$krice<>$kcex<>$kclass<>$karm<>$kbook<>$kbank<>$ksub1<>$ksub2<>$in{'con'}<>$in{'mes'}<>$host<>$date<>$in{'mail'}<>1<><>0<>$in{'con'}<>1<>0<><>A0<>0<>\n");
	}
	open(OUT,">./charalog/main/$in{'id'}.cgi");
	print OUT @new_chara;
	close(OUT);



	if (-d $lockfile) { &UNLOCK_FILE; }
	&DATA_SEND;
	exit;
}

sub mail_to {
	$sendmail = '/usr/lib/sendmail';

	$mail_sub = "�ﱹ�� �������� NET ��� ����";
	&TIME_DATA;

	$a_pass = crypt("$in{'pass'}", wd);

	$mail_msg = <<"EOM";
�ȳ��Ͻʴϱ�? $hi[$in{'chara'}] ��

$GAME_TITLE �� ���迡 ���Ű� ȯ���մϴ�.
��� ������ �Ʒ��� �����Ƿ� �ʽ� Ȯ�����ֽʽÿ�.


�� ����Ͻ� : $daytime
�� ȣ��Ʈ�� : $host
�� �����ڸ� : $hi[$in{'chara'}]
�� �̸��� : $in{'mail'}
�� ���̵� : $in{'id'}
�� ��й�ȣ : $in{'pass'}
�� ����Ű : $a_pass

���� Ű�� ����ؾ����� ���ӿ� ������ �� �ֽ��ϴ�.

[����Ű ����Ϸ� ����]
$SANGOKU_URL/entry.cgi?mode=ATTESTATION
(�� �������κ��� ����� �� �ֽ��ϴ�.)

�׸��� ���� �Խ����� Ȯ���Ͽ� ����� ���������� ���ֺ��� ������ �⸨�ô�.
��, �н����� ���̵���� ������� ���� �����Ƿ� ������ �������ֽʽÿ�.

���̵�� �� ����� �ϳ��ۿ� ������ϴ�.
�������� ��ü���� �����ǰ˻�� whois�� ��Ŀ��� �̿��� �˻絵 �ϰ� �ֽ��ϴ�.
���� ���� ���� �ʴ°� ������ �ͽ��ϴ�.
���� ���ߵǸ� ���ɴ� ���� ������ ���̵���� ���� �����ϴ� �������ּ���.

$GAME_TITLE��� ������

Ȩ������   : http://sam-net.wo.to
EOM

	$mail_msg =~ s/<br>/\n/ig;

	open(MAIL,"| $sendmail -t") || &E_ERR("���� �۽ſ� �����߽��ϴ�.");
	print MAIL "To: $in{'mail'}\n";
	print MAIL "Subject: $mail_sub\n";
	print MAIL "MIME-Version: 1.0\n";
	print MAIL "Content-type: text/plain; charset=euc-kr\n";
	print MAIL "Content-Transfer-Encoding: 8bit\n";
	print MAIL "X-Mailer: $ver\n\n";
	print MAIL "$mail_msg\n";
	close(MAIL);

}

sub E_ERR {

	&HEADER;
	if (-e $lockfile) { unlink($lockfile); }
	print "<center><hr size=0><h3>ERROR !</h3>\n";
	print "<P><font color=red><B>$_[0]</B></font>\n";
print "<form action=\"$FILE_ENTRY\" method=\"post\"><input type=hidden name=id value=$in{'id'}><input type=hidden name=pass value=$in{'pass'}><input type=hidden name=mail value=$in{'mail'}><input type=hidden name=url value=$in{'url'}><input type=hidden name=chara_name value=$hi[$in{'chara'}]><input type=hidden name=mes value=$in{'mes'}><input type=hidden name=mode value=entry><input type=submit value=\"���ƿ´�\"></form>";
	print "<P><hr size=0></center>\n</body></html>\n";
	exit;
}

sub CHEACKER {

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR2("���� ���� ����!");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);


	$num = @CL_DATA;

	if($ENTRY_MAX){
		if($num > $ENTRY_MAX){
			&ERR2("�ִ� ��ϼ� \[$ENTRY_MAX\]�� �Ѱ� �ֽ��ϴ�. ���� �ű� ����� �� �� �����ϴ�.");
		}
	}
}

1;