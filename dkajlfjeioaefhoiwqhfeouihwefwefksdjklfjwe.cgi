#!/usr/bin/perl

require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

require './dataroot/index1.cgi';
require './dataroot/index2.cgi';

if($MENTE) { &ERR2("스크립트 체크를 위해 일시적으로 정지합니다."); }
&DECODE;
&TOP;
&COUNTRY_DATA_OPEN("$kcon");
&CHARA_MAIN_OPEN; 
sub TOP {


	$date = time();
	$month_read = "./log_file/date_count\.cgi";
	open(IN,"$month_read") or &ERR2('파일을 열지 않았습니다.');
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
	$old_date = sprintf("%02d\년%02d\월", $F_YEAR+$myear, $mmonth);

	if($ACT_LOG){
		$actfile = "./log_file/act_log\.cgi";
		open(IN,"$actfile");
		@ACT_DATA = <IN>;
		close(IN);
		($qsec,$qmin,$qhour,$qday) = localtime($date);
		$p=0;
		while($p<5){$A_MES .= "<font color=880000>●</font>$ACT_DATA[$p]<BR>";$p++;}

		$ACT_MES = "<TR><TD bgcolor=#EFE0C0 colspan=\"0\" width=80% height=20><font color=#8E4C28 size=2>$A_MES</font></TD></TR>";

	}

	open(IN,"$DEF_LIST") or &ERR("지정된 파일이 열리지 않습니다.");
	@DEF_DATA = <IN>;
	close(IN);

	open(IN,"$TRAP_LIST");
	@TRAP_DATA = <IN>;
	close(IN);




	open(IN,"$TOWN_LIST") or &ERR("지정된 파일이 열리지 않습니다.");
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
		&MAP_LOG("게임을 개시했습니다.");
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
			unshift(@ACT_DATA,"===============[$myear년$mmonth월]=================\n");
		}

		open(IN,"$COUNTRY_LIST") or &ERR2('파일을 열지 않았습니다. err no :country');
		@COU_DATA = <IN>;
		close(IN);
		@NEW_COU_DATA=();
		foreach(@COU_DATA){
			($xvcid,$xvname,$xvele,$xvmark,$xvking,$xvmes,$xvsub,$xvpri,$xvch)=split(/<>/);
			$xvmark++;
			push(@NEW_COU_DATA,"$xvcid<>$xvname<>$xvele<>$xvmark<>$xvking<>$xvmes<>$xvsub<>$xvpri<>$xvch<>\n");
		}
		open(OUT,">$COUNTRY_LIST") or &ERR('COUNTRY 데이터를 기입할 수 없습니다.');
		print OUT @NEW_COU_DATA;
		close(OUT);

	if($go_ex < 500){
		$sangtae = "건강";
	}elsif($go_ex <1000 && $go_ex > 499){
		$sangtae = "보통";
	}elsif($go_ex < 1250 && $go_ex > 999){
		$sangtae = "나태";
	}elsif($go_ex < 1500 && $go_ex > 1249){
		$sangtae = "중태";
	}elsif($go_ex <1700 && $go_ex > 1499){
		$sangtae = "위험";
	}

		$b_hit = 0;
		if($mmonth eq "1"){
			&MAP_LOG("<img src=$IMG/j11.gif> <font color=orange>세금</font>을 걷고 부하들에게 봉록이 지급되었습니다.");
			$b_hit = 1;
			&K_LOG("$mmonth월 : 현재 상태는 『$sangtae』입니다.");
		}elsif($mmonth eq "7"){
			&MAP_LOG("<img src=$IMG/j12.gif> <font color=orange>수확</font>을 거두었고 부하들에게 쌀이 지급되었습니다.");
			$b_hit = 1;
			&K_LOG("$mmonth월 : 현재 상태는 『$sangtae』입니다.");
		}
		$eve_date = sprintf("%02d\년%02d\월", $F_YEAR+$myear, $mmonth);
		$ihit=0;
	($kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex) = split(/,/,$ksub1);




		if(!int(rand(20))){
			$ihit=1;
			$ino = int(rand(6));
			if($ino eq 0){
				&MAP_LOG("<img src=$IMG/j8.gif> 메뚜기떼들이 밭을 덮쳤습니다!");
				&MAP_LOG2("<img src=$IMG/j8.gif> \[$eve_date\]메뚜기떼들이 밭을 덮쳤습니다!");
			}elsif($ino eq 1){
				&MAP_LOG("<img src=$IMG/j8.gif> 홍수가 일어났습니다! 각지에서 피해가 속출하고 있습니다!");
				&MAP_LOG2("<img src=$IMG/j8.gif> \[$eve_date\]홍수가 일어났습니다! 각지에서 피해가 속출하고 있습니다.");
			}elsif($ino eq 2){
				&MAP_LOG("<img src=$IMG/j8.gif> 역병이 유행하고 있습니다. 거리의 사람들이 괴로워하고 있습니다.");
				&MAP_LOG2("<img src=$IMG/j8.gif> \[$eve_date\]역병이 유행하고 있습니다. 거리의 사람들이 괴로워하고 있습니다.");
			}elsif($ino eq 3){
				&MAP_LOG("<img src=$IMG/j9.gif> 금년은 풍작이 될 것 같습니다.");
				&MAP_LOG2("<img src=$IMG/j9.gif> \[$eve_date\]금년은 풍작이 될 것 같습니다");
			}elsif($ino eq 4){
				&MAP_LOG("<img src=$IMG/j8.gif> 대지진이 일어났습니다.");
				&MAP_LOG2("<img src=$IMG/j8.gif> \[$eve_date\]대지진이 일어났습니다.");
			}elsif($ino eq 5){
				&MAP_LOG("<img src=$IMG/j10.gif> 각 마을의 상점이 활기차 있습니다.");
				&MAP_LOG2("<img src=$IMG/j10.gif> \[$eve_date\]각 마을의 상점이 활기차 있습니다.");
			}elsif($ino eq 6){
				&MAP_LOG("<img src=$IMG/j10.gif> 농민들이 각 지에서 봉기를 일으켰습니다!");
				&MAP_LOG2("<img src=$IMG/j10.gif> \[$eve_date\]농민들이 각 지에서 봉기를 일으켰습니다!");
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
	if($zname eq "성도" || $zname eq "장안" || $zname eq "양양" || $zname eq "낙양" || $zname eq "업" || $zname eq "허창" || $zname eq "건업" || $zname eq "한"){
				$znum_add = int(50 * ($zpri - 50));
	}elsif($zname eq "홍농" || $zname eq "완" || $zname eq "강릉" || $zname eq "여남" || $zname eq "복양" || $zname eq "수춘" || $zname eq "계" || $zname eq "남피" || $zname eq "북해" || $zname eq "하비" || $zname eq "광릉" || $zname eq "오" || $zname eq "국내"){
				$znum_add = int(60 * ($zpri - 50));
	}elsif($zname eq "서량" || $zname eq "한중" || $zname eq "강주" || $zname eq "강하" || $zname eq "장사" || $zname eq "남해" || $zname eq "진유" || $zname eq "시상" || $zname eq "초" || $zname eq "단양" || $zname eq "북평" || $zname eq "회계" || $zname eq "서라벌" || $zname eq "사비" || $zname eq "졸본"){
				$znum_add = int(70 * ($zpri - 50));
	}else{
				$znum_add = int(80 * ($zpri - 50));
	}

				if($znum_add < 500){$znum_add=500;}
				$znum += $znum_add;

	if($zname eq "성도" || $zname eq "장안" || $zname eq "양양" || $zname eq "낙양" || $zname eq "업" || $zname eq "허창" || $zname eq "건업" || $zname eq "한"){
	if($znum > 100000){$znum=100000;}
	}elsif($zname eq "홍농" || $zname eq "완" || $zname eq "강릉" || $zname eq "여남" || $zname eq "복양" || $zname eq "수춘" || $zname eq "계" || $zname eq "남피" || $zname eq "북해" || $zname eq "하비" || $zname eq "광릉" || $zname eq "오" || $zname eq "국내"){
	if($znum > 80000){$znum=80000;}
	}elsif($zname eq "서량" || $zname eq "한중" || $zname eq "강주" || $zname eq "강하" || $zname eq "장사" || $zname eq "남해" || $zname eq "진유" || $zname eq "시상" || $zname eq "초" || $zname eq "단양" || $zname eq "북평" || $zname eq "회계" || $zname eq "서라벌" || $zname eq "사비" || $zname eq "졸본"){
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


	open(IN,"$COUNTRY_LIST") or &ERR2('파일을 열지 않았습니다. err no :country');
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
		$data_mes .= "<TR><Th bgcolor=$ELE_BG[$xxele] colspan=3><font color=$ELE_C[$xxele]>$xxname국</Th></TR><TR><Th bgcolor=$TD_C4>$xxnum명($n_num\%)</Th><Th bgcolor=$TD_C4>$xxgold Gold($n_gold\%)</Th><Th bgcolor=$TD_C4>$xxhp/$xxmaxhp</Th></TR>";
		$c_gold[$i] = $xxgold;
		$c_num[$i] = $xxnum;
		$i++;
	}

	$zmes="";
	$new_date = sprintf("%02d\년%02d\월", $F_YEAR+$myear, $mmonth);
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
		unshift(@E_LOG2,"$_[0]($mday일$hour시$min분)\n");
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
			&ERR2("임시 파일을 작성할 수 없습니다.<br>");
		}elsif(!close(TMP)){			&ERR2("임시 파일을 닫을 수 없습니다.<br>");
		}elsif(!open(DMY,">$tmp_dummy")){
			&ERR2("격납용 일시파일을 작성할 수 없습니다.<br>");
		}elsif(!close(DMY)){
			&ERR2("격납용 일시파일을 닫을 수 없습니다.<br>");
		}elsif(!chmod (0777,"$tmp_dummy")){
			&ERR2("격납용 일시파일의 속성을 변경할 수 없습니다.<br>");
		}elsif(!open(DMY,">$tmp_dummy")){
			&ERR2("격납용 일시파일을 열 수 없습니다.<br>");
		}
		print DMY $data;
		if (!close(DMY)){
			&ERR2("격납용 일시파일을 보존할 수 없습니다.<br>");
		}elsif(!rename("$tmp_dummy" , "$datafile")){
			&ERR2("격납용 일시파일을 데이터 파일에 리네임할 수 없습니다.<br>");
		}elsif(!unlink ("$tmpfile")){
			&ERR2("임시 파일을 삭제할 수 없습니다.<br>");
		}
}

sub K_LOG2 {

	open(IN,"./charalog/log/$kid\.cgi");
	@K_LOG2 = <IN>;
	close(IN);
	unshift(@K_LOG2,"$_[0]($mday일$hour시$min분)\n");
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
		if (--$retry <= 0) { &ERR2("File lock error!<BR>데이터 갱신중입니다. 잠깐 기다려 주세요.");
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