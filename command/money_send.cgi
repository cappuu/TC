sub MONEY_SEND {

	if($in{'no'} eq ""){&ERR("NO:�� �Էµ��� �ʾҽ��ϴ�.");}
	&CHARA_MAIN_OPEN;
	&CHARA_ITEM_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&COUNTRY_DATA_OPEN("$kcon");

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
	@CL_DATA = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];
	foreach(@no){
		$no_list .= "<input type=hidden name=no value=$_>"
	}

	&HEADER;
	$no = $in{'no'} + 1;

	$get_sol = $klea - $ksol;

	if($kskill =~ /Ab/){
		$max = 10000;
	}else{
		$max = 5000;
	}


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
<center><form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<p>[�۱��ϴ� ��븦 ����]<BR><select name=num>
<option value="">�۱��Ϸ��� ����� ����
EOM


	$con_l2 = "<option value=>�� ����λ� \n";
	foreach(@CL_DATA) {
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/);
		if($eid eq $kid) { next; }
		if($cou_name[$econ] eq ""){
			$con_l2 .= "<option value=$eid>$ename\n";
			next;
		}
		if($wcon ne $econ){
			$con_l .= "<option value=>�� $cou_name[$econ]��\n";
		}
		$wcon = $econ;
		$con_l .= "<option value=$eid>$ename\n";
	}

print <<"EOM";
$con_l
$con_l2
</select>
$no_list
<BR><br><font color="red">[�۱ݾ׼� (0 ~ $max)]</font><BR>
<INPUT type=text size=10 name=gold>
<center><br><input type=hidden name=mode value=59>
<input type=submit value="�۱��Ѵ�"></form>


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
<font color="white" face="����"><span style="font-size:9pt;">���� ������ �ٸ� ������� �ڽ��� ���� �۱��� �� �ֽ��ϴ�.<br>�ִ��ѵ����� �� �ϴ� �� 5000�����̸� �ڽ��� ������ �ݾ��� �������� �ϴ� �ݾ׺��� ���ڶ� ��� ���� ���� �����ϴ�.<br>�ڱ��� ���� ������ �ҹ��ϰ� ��� ���̴� �����Ӱ� �۱��� �� �ֽ��ϴ�.<br>���� ������� <font color=red>10%</font>�Դϴ�.</span></font></td>
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
1;