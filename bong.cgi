#!/usr/bin/perl

require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

if($MENTE) { &ERR("�ε����Դϴ�. ��ø� ��ٷ� �ֽʽÿ�."); }
&DECODE;
&TOP;


sub TOP {

	if($in{'num'} eq ""){&ERR("���ð� ���õ��� �ʾҽ��ϴ�.");}

	&CHARA_MAIN_OPEN;

	&TOWN_DATA_OPEN($kpos);
	&COUNTRY_DATA_OPEN($kcon);


	&GWAN2;


	opendir(dirlist,"./charalog/main");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"./charalog/main/$file")){
				&ERR2("���� ���� ����!");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);

	foreach(@CL_DATA) {
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/);
		open(IN,"$TOWN_LIST");
		@TT_DATA = <IN>;
		close(IN);
		($zzname,$zzcon,$zznum,$zznou,$zzsyo,$zzshiro,$zznou_max,$zzsyo_max,$zzshiro_max,$zzpri,$zzx,$zzy,$zzsouba,$zzdef_att,$zzsub1,$zzsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7],$zzname1,$zzname2,$zzbong1,$zzbong2,$zzbong3) = split(/<>/,@TT_DATA[$in{'num'}]);
		if("$zzbong1" eq "$eid"){
			$jjang1 = "$ename";
			$jjang11 = "$echara";
			$jjang111 = "$emes";
		}
		if("$zzbong2" eq "$eid"){
			$jjang2 = "$ename";
			$jjang22 = "$echara";
			$jjang222 = "$emes";
		}
		if("$zzbong3" eq "$eid"){
			$jjang3 = "$ename";
			$jjang33 = "$echara";
			$jjang333 = "$emes";
		}
	}

	&HEADER;
	print <<"EOM";
<body bgcolor="white" text="white" link="blue" vlink="purple" alink="red" leftmargin="0" marginwidth="0" topmargin="0" marginheight="0">
<table align="center" cellpadding="0" cellspacing="0" width="945">
    <tr>
        <td width="945">
            <p><img src="$IMG/up.gif" width="950" height="93" border="0"></p>
        </td>
    </tr>
    <tr>
        <td width="945" height="857" background="$IMG/backg.gif">
            <table align="center" cellpadding="0" cellspacing="0" width="700">
                <tr>
                    <td width="940">
                        <p><img src="$IMG/law1.gif" width="700" height="22" border="0"></p>
                    </td>
                </tr>
                <tr>
                    <td width="940" height="785" background="$IMG/law3.gif">
                        <table valign="up" align="center" cellpadding="0" cellspacing="0" bgcolor="black" width="95%">
                            <tr>
                                <td width="690" height="70">
                                    <p><span style="font-size:9pt;"><b>$town_name[$in{'num'}]���� $kid
                                    �����ϻ�</b><br>$town_name[$in{'num'}]���� ���並 �ϻ��մϴ�.<br>���並 �ϻ��ϰ��� �ϴ� ����� ���� �� 
                                    ���Ͻô� ���� ��ư�� ������ ���� �ϻ��ư�� �����ֽʽÿ�.</span></p>
                                </td>
                            </tr>
                        </table><br>
                        <table border="1" align="center" width="95%">
                            <tr>
                                <td width="655" height="5" colspan="2">
                                    <p align="center">
				    <form action="./bong2.cgi" method="POST">
<select name=jangsu>
<option value="">���並 �ϻ��ϴ� ��� ����
EOM
	foreach(@CL_DATA){
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/);		

		if($kcon eq $econ){
		$con_l .= "<option value=$eid>$ename\n";
		}
}
print <<"EOM";
$con_l
</select>
				    </p>
                                </td>
                            </tr>
                            <tr>
                                <td width="100" height="103">
                                    <table align="center" border="2" cellspacing="0" width="64" height="80" bordercolordark="black" bordercolorlight="black">
                                        <tr>
                                            <td width="64" height="80" background="$IMG/$jjang11.gif">
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                                <td valign="up" width="549" rowspan="2" height="127">
                                   $jjang111
                                </td>
                            </tr>
                            <tr>
                                <td width="100">
				<p align="center"><input type="radio" name="bongto" value="1">[����1] $jjang1
                                </td>
                            </tr>
                            <tr>
                                <td width="100" height="110">
                                    <table align="center" border="2" cellspacing="0" width="64" height="80" bordercolordark="black" bordercolorlight="black">
                                        <tr>
                                            <td width="64" height="80" background="$IMG/$jjang22.gif">
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                                <td valign="up" width="549" rowspan="2" height="138">
                                $jjang222

                                </td>
                            </tr>
                            <tr>
                                <td width="100" height="26">
                                <p align="center"><input type="radio" name="bongto" value="2">[����2] $jjang2</p>
                                </td>
                            </tr>
                            <tr>
                                <td width="100" height="110">
                                    <table align="center" border="2" cellspacing="0" width="64" height="80" bordercolordark="black" bordercolorlight="black">
                                        <tr>
                                            <td width="64" height="80" background="$IMG/$jjang33.gif">
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                                <td valign="up" width="549" rowspan="2" height="128">
                                    $jjang333
                                </td>
                            </tr>
                            <tr>
                                <td width="100" height="16">
                                <p align="center"><input type="radio" name="bongto" value="3">[����3] $jjang3</p>
                                </td>
                            </tr>
                            <tr>
                                <td width="655" height="30" colspan="2">
                                <p align="center">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=num value=$in{'num'}>
<input type=hidden name=mode value=BONG2>
<input type=submit value="���並 �ϻ��Ѵ�"></form>
</p>
                                </td>
                            </tr>
                        </table><br>
                    <table align="center" width="95%" cellpadding="0" cellspacing="0">
                        <tr>
                            <td width="690" bgcolor="black" height="70">
                                <p><span style="font-size:9pt;"><b>$town_name[$in{'num'}]���� ���� ����</b><br>���並 
                                �����մϴ�.<br>�����ϰ��� �ϴ� ��� �� ������ư�� 
                                �����Ѵ��� ������ư�� �����ֽʽÿ�.</span></p>
                            </td>
                        </tr>
                    </table><br>
                    <table border="1" align="center" width="95%">
<form action="./bongtog_d.cgi" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                        <tr>
                            <td width="690" height="12">
                                <input type="radio" name="bongto" value="1">����1(������:$jjang1) <input type="radio" name="bongto" value="2">����2(������:$jjang2) <input type="radio" name="bongto" value="3">����3(������:$jjang3)
                            </td>
                        </tr>
                        <tr>
                            <td width="690" height="30">
                                <p align="center">
	<input type=hidden name=numd value=$in{'num'}>
	<input type=hidden name=mode value=BONGTOG_D>
	<input type=submit value="���並 �����Ѵ�"></form>
				</p>
                            </td>
                        </tr>
                    </table>
<form action=\"mydata.cgi\" method=\"post\">
                <p align="center"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM><input type=submit value=\"���ƿ´�\"></form>
                    </td>
                </tr>
                <tr>
                    <td width="940">
                        <p><img src="$IMG/law2.gif" width="700" height="22" border="0"></p>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
    <tr>
        <td width="945">
            <p><img src="$IMG/down.gif" width="950" height="26" border="0"></p>
        </td>
    </tr>
</table>
</body>
EOM

	&FOOTER;
	exit;

}