#!/usr/bin/perl

require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

if($MENTE) { &ERR2("��ũ��Ʈ üũ�� ���� �Ͻ������� �����մϴ�."); }
&DECODE;
&COUNTRY_DATA_OPEN("$kcon");
&CHARA_MAIN_OPEN;

if($mode eq 'TOP') { &TOP; }
elsif($mode eq 'TOP_NEW'){&TOP_NEW;}
else{&TOP0;}



sub TOP_NEW {
	&CHARA_MAIN_OPEN;
	&CHARA_ITEM_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&COUNTRY_DATA_OPEN("$kcon");

	if($jin_ex){
		&ERR('�̹� ������ �����Դϴ�.');
	}

	open(IN,"./log_file/event_on.cgi");
	@EVENT = <IN>;
	close(IN);

	($eventon,$emoney,$etime) = split(/<>/,$EVENT[0]);

	$emoney += 100;

	@EVENT_DATA=();
	unshift(@EVENT_DATA,"$eventon<>$emoney<>$etime<>");
	open(OUT,">./log_file/event_on.cgi") or &ERR('MAIN ���ο� �����͸� ������ �� �����ϴ�.');
	print OUT @EVENT_DATA;
	close(OUT);

	$kgold -= 100;
	$jin_ex += 1;

	$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
	&CHARA_MAIN_INPUT;
	&HEADER;
print <<"EOM";
<CENTER><hr size=0><h2>�� 100�� �����ϰ� ���ִ�ȸ�� �����Ͽ����ϴ�. [�Ѵ����ݾ� : $emoney]</h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="Ȯ��"></form></CENTER>
EOM

	&FOOTER;

	exit;

}




sub TOP0 {
	&CHARA_MAIN_OPEN;
	&CHARA_ITEM_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&COUNTRY_DATA_OPEN("$kcon");



	if($jin_ex eq ""){
		&ERR('��û���� ���� �����̰ų� ���� �̹� Ż���� �����Դϴ�.');
	}

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

	@tmp = map {(split /<>/)[10]} @CL_DATA;
	@CL_DATA = @CL_DATA[sort {rand} 0 .. $#tmp];
	foreach(@no){
		$no_list .= "<input type=hidden name=no value=$_>"
	}


	$thing = 0;
	foreach(@CL_DATA) {
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/);
		($estr_ex,$eint_ex,$elea_ex,$echa_ex,$esub1_ex,$esub2_ex,$ebo_ex,$egi_ex,$ech_ex,$egu_ex,$ego_ex,$ejin_ex) = split(/,/,$esub1);			
		if($ejin_ex == 1){ 
		$thing++;
		}
	}


	if($thing == 1){
	open(IN,"./log_file/event_on.cgi");
	@EVENT = <IN>;
	close(IN);

	($eventon,$emoney) = split(/<>/,$EVENT[0]);
		$kgold += $emoney;
		&CHARA_MAIN_INPUT;

		$emoney = 0;
		$eventon = 3;
	@EVENT_DATA=();
	unshift(@EVENT_DATA,"$eventon<>$emoney<>");
	open(OUT,">./log_file/event_on.cgi") or &ERR('MAIN ���ο� �����͸� ������ �� �����ϴ�.');
	print OUT @EVENT_DATA;
	close(OUT);
		&MAP_LOG("<img src=$IMG/j27.gif> õ�Ϲ��ִ�ȸ���� $kname���� ����� �Ÿ�������ϴ�!");


	@NEW_DATA = ();

	$timefile = "./log_file/event_time.cgi";
	open(OUT,">$timefile");
	print OUT @NEW_DATA;
	close(OUT);

		&ERR('[�� <b>���</b> ��]<br>�����մϴ�.<br>������ 1�α��� ���ҽ��ϴ�.<br>��� $emoney �� ȹ���ϼ̽��ϴ�!');


	}


	&HEADER;
	$no = $in{'no'} + 1;

	$get_sol = $klea - $ksol;
	print <<"EOM";
<STYLE>BODY {
	CURSOR: url('samnet.cur')
}
A {
	CURSOR: url('samnet.ani'); TEXT-DECORATION: none
}
</STYLE>
<BODY oncontextmenu="return false" onselectstart="return false" ondragstart="return false">
<table align="center" width="950">
    <tr>
        <td>
            <img src="$IMG/up.gif">
        </td>
    </tr>
    <tr height="600">
        <td background="$IMG/backg.gif">
<table align="center" border="1" cellspacing="0" width="752" height="492" bordercolordark="white" bordercolorlight="black">
    <tr>
        <td width="1101" height="492" background="$IMG/cola.jpg">
            <table cellpadding="0" cellspacing="0" width="752" height="488" bordercolordark="white" bordercolorlight="black" background="$IMG/cola.jpg">
                <tr>
                    <td width="752" height="22" colspan="8">
                        <p>&nbsp;</p>
                    </td>
                </tr>
                <tr>
                    <td width="11" height="467" rowspan="6">
                        <p>&nbsp;</p>
                    </td>
                    <td width="52" height="236" rowspan="4">
                        <p>&nbsp;</p>
                    </td>
                    <td width="141" height="236" rowspan="4">
                        <table cellpadding="0" cellspacing="0">
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$cou_name[$kcon]</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$kstrt</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$kintt</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$kleat</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$kchat</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$kgold</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$krice</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$kcex</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$ksol</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$kgat</span></font></p>
                                </td>
                            </tr>
                        </table>

                    </td>
                    <td width="25" height="236" rowspan="4">
                    </td>
                    <td width="70" height="34">
                    </td>
                    <td width="24" height="236" rowspan="4">
                  </td>
                    <td width="421" height="467" rowspan="6">
<TABLE border=0 width=100% height=80%><TR><TD>
<center><form action=event.cgi method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<p>[�ϱ���&���� ��븦 ����]<BR><select name=num>
<option value="">����� ����
EOM


	foreach(@CL_DATA) {
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/);
		($estr_ex,$eint_ex,$elea_ex,$echa_ex,$esub1_ex,$esub2_ex,$ebo_ex,$egi_ex,$ech_ex,$egu_ex,$ego_ex,$ejin_ex) = split(/,/,$esub1);			
		if($eid eq $kid) { next; }
		if($ejin_ex == 1){
		if($econ eq "" || $econ eq 0){
		$con_l2 .= "<option value=$eid>????? ����ߡ�\n";
		}else{
		$con_l2 .= "<option value=$eid>????? ��$cou_name[$econ]��\n";
		}
		}
	}

print <<"EOM";
$con_l
$con_l2
</select>
$no_list
<BR><br>[�ܷ�� ���]<br>
<select name=ilgiselect size="1">
<option value="1">�ϱ���� �º� (����,��� ����)
<option value="2">�������� �º� (����,�ŷ� ����)
</select>
<center><br><input type=hidden name=mode value=TOP>
<input type=submit value="õ�Ϲ��ִ�ȸ����"></form>


<center><form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="���ƿ´�"></center></center></form></CENTER>
</TD></TR></TABLE>
                    </td>
                    <td width="8" height="467" rowspan="6">
                    </td>
                </tr>
                <tr>
                    <td width="70" height="82">
                        <p align="center"><img src="$IMG/$kchara.gif" width="64" height="80" border="0"></p>
                    </td>
                </tr>
                <tr>
                    <td width="70" height="37">
                        <p align="center"><font color="white" face="����"><span style="font-size:9pt;">$kname</span></font></p>
                    </td>
                </tr>
                <tr>
                    <td width="70" height="83">
                    </td>
                </tr>
                <tr>
                    <td width="312" height="35" colspan="5">
                    </td>
                </tr>
                <tr>
                    <td width="288" height="196" colspan="4" valign="up">
<font color="white" face="����"><span style="font-size:9pt;">�������� �𸣴� ������ ���� �ڽ��ִ� �ܷ�������� ����մϴ�.<br>���� ������ �𸣱� ������ �ܷ������ �� �����ϼž� �մϴ�.<br>���� ���� ������ Ż���̰� ������ 1���� ���������� ����ؼ� �ο�ϴ�.</span></font></td>
                    <td width="24" height="196">
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
        </td>
    </tr>
    <tr>
        <td>
            <img src="$IMG/down.gif">
        </td>
    </tr>
</table>

EOM

	&FOOTER;

	exit;

}






sub TOP{

	&EVENT_TIME_LIST;




							open(IN,"./charalog/main/$in{'num'}\.cgi");
							@E_DATA = <IN>;
							close(IN);
							($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/,$E_DATA[0]);
							($estr_ex,$eint_ex,$elea_ex,$echa_ex,$esub1_ex,$esub2_ex,$ebo_ex,$egi_ex,$ech_ex,$egu_ex,$ego_ex,$ejin_ex) = split(/,/,$esub1);

							
										&CHARA_ITEM_OPEN;

										$kche = 100;
										$eche = 100;

										if($in{'ilgiselect'} == 1){
										&K_LOG4("\[���ִ�ȸ\]$ename(����:$estrt ���:$eleat)�԰� �ϱ��並 ����!");
										&E_LOG4("\[���ִ�ȸ\]$kname(����:$kstrt ���:$kleat)�԰� �ϱ��並 ����!");



										for($count=1;$count<60;$count++){

										if($kche <= 0){last;}

										$kdmge = int((($kstrt+$kleat)/50)+rand(($kstrt+$kleat)/10));
										$edmge = int((($estrt+$eleat)/50)+rand(($estrt+$eleat)/10));

										if($kdmge < 1){
											$kdmge=1;	
										}

							

										$eche -= $kdmge;

										if($eche <= 0){
											&K_LOG4("<font color=red>$count</font>��:$kname�� ü�� $kche (-$edmge\) VS $ename�� ü�� $eche (-$kdmge\)");
											&E_LOG4("<font color=red>$count</font>��:$kname�� ü�� $kche (-$edmge\) VS $ename�� ü�� $eche (-$kdmge\)");
											$wine = 1;
										last;
										}
										
										if($edmge < 1){
											$edmge=1;	
										}

										$kche -= $edmge;

										if($kche <= 0){
											&K_LOG4("<font color=red>$count</font>��:$kname�� ü�� $kche (-$edmge\) VS $ename�� ü�� $eche (-$kdmge\)");
											&E_LOG4("<font color=red>$count</font>��:$kname�� ü�� $kche (-$edmge\) VS $ename�� ü�� $eche (-$kdmge\)");
											last;
										}
										&K_LOG4("<font color=red>$count</font>��:$kname�� ü�� $kche (-$edmge\) VS $ename�� ü�� $eche (-$kdmge\)");
										}




										if($wine){

										&K_LOG4("\[���ִ�ȸ]$kname���� $ename���� ���� �ϱ��信�� �¸�!");
										&E_LOG4("\[���ִ�ȸ]$kname���� $ename���� ���� �ϱ��信�� �¸�!");
										$ejin_ex = "";
										$esub1 = "$estr_ex,$eint_ex,$elea_ex,$echa_ex,$esub1_ex,$esub2_ex,$ebo_ex,$egi_ex,$ech_ex,$egu_ex,$ego_ex,$ejin_ex,";
										&ENEMY_INPUT;
										}else{
										&K_LOG4("\[���ִ�ȸ]$ename���� $kname���� ���� �ϱ��信�� �¸�!");
										&E_LOG4("\[���ִ�ȸ]$ename���� $kname���� ���� �ϱ��信�� �¸�!");
										$jin_ex = "";
										$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
										&CHARA_MAIN_INPUT;
										}

										}elsif($in{'ilgiselect'} == 2){

										&K_LOG4("\[���ִ�ȸ]$ename(����:$eintt �ŷ�:$echat)�԰� ������ ����!");
										&E_LOG4("\[���ִ�ȸ]$kname(����:$kintt �ŷ�:$kchat)�԰� ������ ����!");
										for($count=1;$count<60;$count++){

										if($kche <= 0){last;}

										$kdmge = int((($kintt+$kchat)/50)+rand(($kintt+$kchat)/10));
										$edmge = int((($eintt+$echat)/50)+rand(($eintt+$echat)/10));

										if($kdmge < 1){
											$kdmge=1;	
										}

							

										$eche -= $kdmge;

										if($eche <= 0){
											$eche = 0;
											&K_LOG4("<font color=red>$count</font>ȸ:$kname�� ���ŷ� $kche (-$edmge\) VS $ename�� ���ŷ� $eche (-$kdmge\)");
											&E_LOG4("<font color=red>$count</font>ȸ:$kname�� ���ŷ� $kche (-$edmge\) VS $ename�� ���ŷ� $eche (-$kdmge\)");
											$wine1 = 1;
										last;
										}
										
										if($edmge < 1){
											$edmge=1;	
										}

										$kche -= $edmge;

										if($kche <= 0){
											$kche = 0;
											&K_LOG4("<font color=red>$count</font>ȸ:$kname�� ���ŷ� $kche (-$edmge\) VS $ename�� ���ŷ� $eche (-$kdmge\)");
											&E_LOG4("<font color=red>$count</font>ȸ:$kname�� ���ŷ� $kche (-$edmge\) VS $ename�� ���ŷ� $eche (-$kdmge\)");
											last;
										}
										&K_LOG4("<font color=red>$count</font>ȸ:$kname�� ���ŷ� $kche (-$edmge\) VS $ename�� ���ŷ� $eche (-$kdmge\)");
										}
										if($wine1){
										&K_LOG4("\[���ִ�ȸ]$kname���� $ename���� ���� �������� �¸�!");
										&E_LOG4("\[���ִ�ȸ]$kname���� $ename���� ���� �������� �¸�!");
										$ejin_ex = "";
										$esub1 = "$estr_ex,$eint_ex,$elea_ex,$echa_ex,$esub1_ex,$esub2_ex,$ebo_ex,$egi_ex,$ech_ex,$egu_ex,$ego_ex,$ejin_ex,";
										&ENEMY_INPUT;
										}else{
										&K_LOG4("\[���ִ�ȸ]$ename���� $kname���� ���� �������� �¸�!");
										&E_LOG4("\[���ִ�ȸ]$ename���� $kname���� ���� �������� �¸�!");
										$jin_ex = "";
										$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
										&CHARA_MAIN_INPUT;
										}
										}







	open(IN,"./charalog/log3/$kid.cgi");
	@LOG_DATA2 = <IN>;
	close(IN);
	$p=0;
	while($p<20){$log_list2 .= "<font color=navy>��</font>$LOG_DATA2[$p]<BR>";$p++;}							


	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>$ename�԰� �ºθ� �ܷ���ϴ�.</h2><p>
$log_list2
<form action="./event.cgi" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=submit value="Ȯ��"></form></CENTER>
EOM

	&FOOTER;

	exit;

							}