#!/usr/bin/perl

require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

require './dataroot/index1.cgi';
require './dataroot/index2.cgi';

if($MENTE) { &ERR2("��ũ��Ʈ üũ�� ���� �Ͻ������� �����մϴ�."); }
&DECODE;
&TOP;
&COUNTRY_DATA_OPEN("$kcon");
&CHARA_MAIN_OPEN; 
sub TOP {


	$date = time();
	$month_read = "./log_file/date_count\.cgi";
	open(IN,"$month_read") or &ERR2('������ ���� �ʾҽ��ϴ�.');
	@MONTH_DATA = <IN>;
	close(IN);
	&TIME_DATA;

	open(IN,"$MAP_LOG_LIST");
	@S_MOVE = <IN>;
	close(IN);
	$p=0;
	while($p<12){$S_MES .= "&nbsp;$S_MOVE[$p]<BR>";$p++;}

	open(IN,"$MAP_LOG_LIST2");
	@S_MOVE = <IN>;
	close(IN);
	$p=0;
	while($p<11){$D_MES .= "&nbsp;$S_MOVE[$p]<BR>";$p++;}

	open(IN,"$MAP_LOG_LIST3");
	@S_MOVE = <IN>;
	close(IN);
	$p=0;
	while($p<4){$G_MES .= "&nbsp;$S_MOVE[$p]<BR>";$p++;}

	$hit = 0;
	@month_new=();

	($myear,$mmonth,$mtime) = split(/<>/,$MONTH_DATA[0]);
	$old_date = sprintf("%02d\��%02d\��", $F_YEAR+$myear, $mmonth);

	if($ACT_LOG){
		$actfile = "./log_file/act_log\.cgi";
		open(IN,"$actfile");
		@ACT_DATA = <IN>;
		close(IN);
		($qsec,$qmin,$qhour,$qday) = localtime($date);
		$p=0;
		while($p<5){$A_MES .= "<font color=880000>��</font>$ACT_DATA[$p]<BR>";$p++;}

		$ACT_MES = "<TR><TD bgcolor=#EFE0C0 colspan=\"0\" width=80% height=20><font color=#8E4C28 size=2>$A_MES</font></TD></TR>";

	}

	open(IN,"$DEF_LIST") or &ERR("������ ������ ������ �ʽ��ϴ�.");
	@DEF_DATA = <IN>;
	close(IN);

	open(IN,"$TRAP_LIST");
	@TRAP_DATA = <IN>;
	close(IN);




	open(IN,"$TOWN_LIST") or &ERR("������ ������ ������ �ʽ��ϴ�.");
	@TOWN_DATA = <IN>;
	close(IN);
	($zwname,$wzc)=split(/<>/,$TOWN_DATA[0]);
	$zzhit=0;
	foreach(@TOWN_DATA){
		($zwname,$zwcon)=split(/<>/);
			if($wzc ne $zwcon){$zzhit=1;}
			$wzc = $zwcon;
	}


	&CHEACK_COM;
	if($mtime + $TIME_REMAKE < $date){
		if($mtime eq ""){
		$mtime = $date;
		&MAP_LOG("������ �����߽��ϴ�.");
		}else{
		$mtime += $TIME_REMAKE;
		}
		$mmonth++;
		if($mmonth > 12){
			$myear++;
			$mmonth=1;
		}
		unshift(@month_new,"$myear<>$mmonth<>$mtime<>\n");
		if($ACT_LOG){
			($qsec,$qmin,$qhour,$qday) = localtime($mtime);
			unshift(@ACT_DATA,"===============[$myear��$mmonth��]=================\n");
		}

		open(IN,"$COUNTRY_LIST") or &ERR2('������ ���� �ʾҽ��ϴ�. err no :country');
		@COU_DATA = <IN>;
		close(IN);
		@NEW_COU_DATA=();
		foreach(@COU_DATA){
			($xvcid,$xvname,$xvele,$xvmark,$xvking,$xvmes,$xvsub,$xvpri,$xvch)=split(/<>/);
			$xvmark++;
			push(@NEW_COU_DATA,"$xvcid<>$xvname<>$xvele<>$xvmark<>$xvking<>$xvmes<>$xvsub<>$xvpri<>$xvch<>\n");
		}
		open(OUT,">$COUNTRY_LIST") or &ERR('COUNTRY �����͸� ������ �� �����ϴ�.');
		print OUT @NEW_COU_DATA;
		close(OUT);

	if($go_ex < 500){
		$sangtae = "�ǰ�";
	}elsif($go_ex <1000 && $go_ex > 499){
		$sangtae = "����";
	}elsif($go_ex < 1250 && $go_ex > 999){
		$sangtae = "����";
	}elsif($go_ex < 1500 && $go_ex > 1249){
		$sangtae = "����";
	}elsif($go_ex <1700 && $go_ex > 1499){
		$sangtae = "����";
	}

		$b_hit = 0;
		if($mmonth eq "1"){
			&MAP_LOG("<img src=$IMG/j11.gif> <font color=orange>����</font>�� �Ȱ� ���ϵ鿡�� ������ ���޵Ǿ����ϴ�.");
			$b_hit = 1;
			&K_LOG("$mmonth�� : ���� ���´� ��$sangtae���Դϴ�.");
		}elsif($mmonth eq "7"){
			&MAP_LOG("<img src=$IMG/j12.gif> <font color=orange>��Ȯ</font>�� �ŵξ��� ���ϵ鿡�� ���� ���޵Ǿ����ϴ�.");
			$b_hit = 1;
			&K_LOG("$mmonth�� : ���� ���´� ��$sangtae���Դϴ�.");
		}
		$eve_date = sprintf("%02d\��%02d\��", $F_YEAR+$myear, $mmonth);
		$ihit=0;
	($kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex) = split(/,/,$ksub1);




		if(!int(rand(20))){
			$ihit=1;
			$ino = int(rand(6));
			if($ino eq 0){
				&MAP_LOG("<img src=$IMG/j8.gif> �޶ѱⶼ���� ���� ���ƽ��ϴ�!");
				&MAP_LOG2("<img src=$IMG/j8.gif> \[$eve_date\]�޶ѱⶼ���� ���� ���ƽ��ϴ�!");
			}elsif($ino eq 1){
				&MAP_LOG("<img src=$IMG/j8.gif> ȫ���� �Ͼ���ϴ�! �������� ���ذ� �����ϰ� �ֽ��ϴ�!");
				&MAP_LOG2("<img src=$IMG/j8.gif> \[$eve_date\]ȫ���� �Ͼ���ϴ�! �������� ���ذ� �����ϰ� �ֽ��ϴ�.");
			}elsif($ino eq 2){
				&MAP_LOG("<img src=$IMG/j8.gif> ������ �����ϰ� �ֽ��ϴ�. �Ÿ��� ������� ���ο��ϰ� �ֽ��ϴ�.");
				&MAP_LOG2("<img src=$IMG/j8.gif> \[$eve_date\]������ �����ϰ� �ֽ��ϴ�. �Ÿ��� ������� ���ο��ϰ� �ֽ��ϴ�.");
			}elsif($ino eq 3){
				&MAP_LOG("<img src=$IMG/j9.gif> �ݳ��� ǳ���� �� �� �����ϴ�.");
				&MAP_LOG2("<img src=$IMG/j9.gif> \[$eve_date\]�ݳ��� ǳ���� �� �� �����ϴ�");
			}elsif($ino eq 4){
				&MAP_LOG("<img src=$IMG/j8.gif> �������� �Ͼ���ϴ�.");
				&MAP_LOG2("<img src=$IMG/j8.gif> \[$eve_date\]�������� �Ͼ���ϴ�.");
			}elsif($ino eq 5){
				&MAP_LOG("<img src=$IMG/j10.gif> �� ������ ������ Ȱ���� �ֽ��ϴ�.");
				&MAP_LOG2("<img src=$IMG/j10.gif> \[$eve_date\]�� ������ ������ Ȱ���� �ֽ��ϴ�.");
			}elsif($ino eq 6){
				&MAP_LOG("<img src=$IMG/j10.gif> ��ε��� �� ������ ���⸦ �����׽��ϴ�!");
				&MAP_LOG2("<img src=$IMG/j10.gif> \[$eve_date\]��ε��� �� ������ ���⸦ �����׽��ϴ�!");
			}
		}
		if($b_hit){
		@NEW_TOWN_DATA=();
		foreach(@TOWN_DATA){
			($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7],$zname1,$zname2,$zbong1,$zbong2,$zbong3)=split(/<>/);
			if(!int(rand(2.0))){
				$zsouba += int(rand(0.5)*100)/100;
				if($zsouba > 1.2){
					$zsouba = 1.2;
				}
			}else{
				$zsouba -= int(rand(0.5)*100)/100;
				if($zsouba < 0.8){
					$zsouba = 0.8;
				}
			}
			if($zpri >= 50){
	if($zname eq "����" || $zname eq "���" || $zname eq "���" || $zname eq "����" || $zname eq "��" || $zname eq "��â" || $zname eq "�Ǿ�" || $zname eq "��"){
				$znum_add = int(50 * ($zpri - 50));
	}elsif($zname eq "ȫ��" || $zname eq "��" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "��" || $zname eq "����" || $zname eq "����" || $zname eq "�Ϻ�" || $zname eq "����" || $zname eq "��" || $zname eq "����"){
				$znum_add = int(60 * ($zpri - 50));
	}elsif($zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "���" || $zname eq "����" || $zname eq "����" || $zname eq "�û�" || $zname eq "��" || $zname eq "�ܾ�" || $zname eq "����" || $zname eq "ȸ��" || $zname eq "�����" || $zname eq "���" || $zname eq "����"){
				$znum_add = int(70 * ($zpri - 50));
	}else{
				$znum_add = int(80 * ($zpri - 50));
	}

				if($znum_add < 500){$znum_add=500;}
				$znum += $znum_add;

	if($zname eq "����" || $zname eq "���" || $zname eq "���" || $zname eq "����" || $zname eq "��" || $zname eq "��â" || $zname eq "�Ǿ�" || $zname eq "��"){
	if($znum > 100000){$znum=100000;}
	}elsif($zname eq "ȫ��" || $zname eq "��" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "��" || $zname eq "����" || $zname eq "����" || $zname eq "�Ϻ�" || $zname eq "����" || $zname eq "��" || $zname eq "����"){
	if($znum > 80000){$znum=80000;}
	}elsif($zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "���" || $zname eq "����" || $zname eq "����" || $zname eq "�û�" || $zname eq "��" || $zname eq "�ܾ�" || $zname eq "����" || $zname eq "ȸ��" || $zname eq "�����" || $zname eq "���" || $zname eq "����"){
	if($znum > 65000){$znum=65000;}
	}else{
	if($znum > 50000){$znum=50000;}
	}

			}else{
				$znum -= int(80 * (50 - $zpri));
			}
			if($ihit){
				if($ino eq 0){
					$znou = int($znou * 0.8);
				}elsif($ino eq 1){
					$znou = int($znou * 0.9);
					$zsyo = int($zsyo * 0.9);
					$zshiro = int($zshiro * 0.9);
				}elsif($ino eq 2){
					$znum = int($znum * 0.8);
				}elsif($ino eq 3){
					$znou = int($znou * 1.2);
					if($znou > $znou_max){$znou=$znou_max;}
				}elsif($ino eq 4){
					$znou = int($znou * 0.8);
					$zsyo = int($zsyo * 0.8);
					$zshiro = int($zshiro * 0.8);
					$znum = int($znum * 0.9);
				}elsif($ino eq 5){
					$zsyo = int($zsyo * 1.1);
					if($zsyo > $zsyo_max){$zsyo=$zsyo_max;}
				}elsif($ino eq 6 && zpri < 20){
					$zcon = "";
					$znou = int($znou*0.8);
					$zsyo = int($zsyo*0.8);
					$znum = int($znum*0.8);
					$zsub1 = int($zsub1*0.8);
					$zshiro += 100;
					$zpri = int($zpri*0.8);
					$zdef_att = int($zdef_att*0.8);
				}
			}

			push(@NEW_TOWN_DATA,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");
		}
		open(OUT,">$TOWN_LIST");
		print OUT @NEW_TOWN_DATA;
		close(OUT);
		}
		open(OUT,">$month_read");
		print OUT @month_new;
		close(OUT);

	}
	if($ACT_LOG){
		if(@ACT_DATA > 800) { splice(@ACT_DATA,800); }
		open(OUT,">$actfile");
		print OUT @ACT_DATA;
		close(OUT);
	}


	open(IN,"$COUNTRY_LIST") or &ERR2('������ ���� �ʾҽ��ϴ�. err no :country');
	@COU_DATA = <IN>;
	close(IN);
	foreach(@COU_DATA){
		($x2cid,$x2name,$x2ele,$x2mark)=split(/<>/);
		$cou_name[$x2cid] = "$x2name";
		$cou_ele[$x2cid] = "$x2ele";
		$cou_mark[$x2cid] = "$x2mark";
	}


	$country_no=0;$i=1;
	foreach(@COU_DATA){
		($xxcid,$xxname,$xxele,$xxnum,$xxins,$xxind,$xxall,$xxgold,$xxhp,$xxmaxhp,$xxstr,$xxvit,$xxagi)=split(/<>/);
		if($all_gold){
		$n_gold = int(($xxgold/($all_gold))*1000)/10;
		}else{
		$n_gold = 0;
		}
		if($all_num){
		$n_num  = int(($xxnum/($all_num))*1000)/10;
		}else{
		$n_num  = 0;
		}
		$data_mes .= "<TR><Th bgcolor=$ELE_BG[$xxele] colspan=3><font color=$ELE_C[$xxele]>$xxname��</Th></TR><TR><Th bgcolor=$TD_C4>$xxnum��($n_num\%)</Th><Th bgcolor=$TD_C4>$xxgold Gold($n_gold\%)</Th><Th bgcolor=$TD_C4>$xxhp/$xxmaxhp</Th></TR>";
		$c_gold[$i] = $xxgold;
		$c_num[$i] = $xxnum;
		$i++;
	}

	$zmes="";
	$new_date = sprintf("%02d\��%02d\��", $F_YEAR+$myear, $mmonth);
	$next_time = int(($mtime + $TIME_REMAKE - $date) / 60);

	&HEADER;

	&CHILRANG_INDEX;

	exit;

}

	&CHECK_COM;


sub E_LOG2 {
	if($eid ne ""){
		open(IN,"./charalog/log/$eid\.cgi");
		@E_LOG2 = <IN>;
		close(IN);
		unshift(@E_LOG2,"$_[0]($mday��$hour��$min��)\n");
		splice(@E_LOG2,20);

		open(OUT,">./charalog/log/$eid\.cgi");
		print OUT @E_LOG2;
		close(OUT);
	}
}

sub data_save {
        local($datapath) = $_[0];
		local($file) = $_[1];
		local($data) = "$_[2]";
		local($datafile) = $datapath . '/' . $file;
		local($tmpfile) = $datapath . '/' . $file . '.tmp';
		local($tmp_dummy) = $datapath . '/' . $file . "$$\.tmp";
		local($datadir) = $datapath . '/';
		opendir(DIR, $datadir) ;
		@list = readdir(DIR) ;
		closedir(DIR) ;

		if(!open(TMP,">$tmpfile")){
			&ERR2("�ӽ� ������ �ۼ��� �� �����ϴ�.<br>");
		}elsif(!close(TMP)){			&ERR2("�ӽ� ������ ���� �� �����ϴ�.<br>");
		}elsif(!open(DMY,">$tmp_dummy")){
			&ERR2("�ݳ��� �Ͻ������� �ۼ��� �� �����ϴ�.<br>");
		}elsif(!close(DMY)){
			&ERR2("�ݳ��� �Ͻ������� ���� �� �����ϴ�.<br>");
		}elsif(!chmod (0777,"$tmp_dummy")){
			&ERR2("�ݳ��� �Ͻ������� �Ӽ��� ������ �� �����ϴ�.<br>");
		}elsif(!open(DMY,">$tmp_dummy")){
			&ERR2("�ݳ��� �Ͻ������� �� �� �����ϴ�.<br>");
		}
		print DMY $data;
		if (!close(DMY)){
			&ERR2("�ݳ��� �Ͻ������� ������ �� �����ϴ�.<br>");
		}elsif(!rename("$tmp_dummy" , "$datafile")){
			&ERR2("�ݳ��� �Ͻ������� ������ ���Ͽ� �������� �� �����ϴ�.<br>");
		}elsif(!unlink ("$tmpfile")){
			&ERR2("�ӽ� ������ ������ �� �����ϴ�.<br>");
		}
}

sub K_LOG2 {

	open(IN,"./charalog/log/$kid\.cgi");
	@K_LOG2 = <IN>;
	close(IN);
	unshift(@K_LOG2,"$_[0]($mday��$hour��$min��)\n");
	splice(@K_LOG2,20);
	open(OUT,">./charalog/log/$kid\.cgi");
	print OUT @K_LOG2;
	close(OUT);
}


sub SALARY {

	$ksal=0;
	foreach(@TOWN_DATA){
		($z2name,$z2con,$z2num,$z2nou,$z2syo,$z2shiro)=split(/<>/);
		if($z2con eq $kcon){
			if($mmonth eq "1"){
				$ksal += int($z2syo * 8 * $z2num / 16000);
			}elsif($mmonth eq "7"){
				$ksal += int($z2nou * 8 * $z2num / 16000);
			}
		}
	}
}


sub D_F_LOCK {

	local($retry)=1;
	if (-e $lockfile2) {
		local($mtime) = (stat($lockfile2))[9];
		if ($mtime && $mtime < time - 60) { &D_UNLOCK_FILE; }
	}

	while (!mkdir($lockfile2, 0755)) {
		if (--$retry <= 0) { &ERR2("File lock error!<BR>������ �������Դϴ�. ��� ��ٷ� �ּ���.");
}
		sleep(1);
	}
}

sub D_UNLOCK_FILE
{
  rmdir("$lockfile2");
}




sub TOWN_CHANGE{

	local($townpos) = $_[0];

	splice(@TOWN_DATA,$townpos,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");

}

sub lock #($file_name, $use_lock)
{
	local($file_name, $use_lock) = @_;
	local($lock_flag) = $file_name . ".lock";

	if ($use_lock) {
	local($i) = 0;
#	return -1 if (!-f $file_name);
	rmdir($lock_flag) if (-d $lock_flag && time - (stat($lock_flag))[9] > 60);
	while(!mkdir($lock_flag, 0755)) {	select(undef, undef, undef, 0.05);
		return 0 if (++ $i >= 100);
		}
		return 1;
 	}
 	return 1;
}

sub unlock
{
  rmdir("$_[0].lock") if (-d "$_[0].lock");
}