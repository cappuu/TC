sub ENTRY {
	&CHEACKER;
	&HEADER;

	open(IN,"./log_file/country.cgi") or &E_ERR('������ ���� �ʾҽ��ϴ�. err no :country');
	@COU_DATA1 = <IN>;
	close(IN);

	open(IN,"$COUNTRY_LIST") or &ERR2('������ ���� �ʾҽ��ϴ�.');
	@COU_DATA = <IN>;
	close(IN);

	open(IN,"$COUNTRY_MES") or &ERR("������ ������ ������ �ʽ��ϴ�.");
	@MES_DATA = <IN>;
	close(IN);

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

	foreach(@CL_DATA) {
	($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$kskill,$kpoint,$kct,$klevel,$kexp,$kcodea,$kcodeb,$kqpoint) = split(/<>/);
	if($hi[$kchara] eq $kname){
	$hi[$kchara]++;
	$hi[$kchara]="$kname���Ұ���";
	}
	}


	open(IN,"./charalog/main/$in{'id'}.cgi");
	@NEWCHARA = <IN>;
	close(IN);

	open(IN,"$COUNTRY_LIST") or &ERR2('������ ���� �ʾҽ��ϴ�. err no :country');
	@COU_DATA = <IN>;
	close(IN);
	foreach(@COU_DATA){
		($x2cid,$x2name,$x2ele,$x2mark)=split(/<>/);
		$cou_name[$x2cid] = "$x2name";
		$cou_ele[$x2cid] = "$x2ele";
		$cou_mark[$x2cid] = "$x2mark";
	}

	$type_check{$in{'type'}} = "checked";

	$mess .= "<TR><TD BGCOLOR=272123 colspan=2><center><img src=$IMG/gonggo.gif></TD></TR>";
	foreach(@MES_DATA){
		($cmes,$cid)=split(/<>/);
		$mess .= "<TR><TD bgcolor=$ELE_C[$cou_ele[$cid]]><center>$cou_name[$cid]</TD><TD bgcolor=$ELE_C[$cou_ele[$cid]]>$cmes</TD></TR>";
	}

	open(IN,"$TOWN_LIST") or &ERR("������ ������ ������ �ʽ��ϴ�.");
	@TOWN_DATA = <IN>;
	close(IN);

	$zc=0;

	foreach(@TOWN_DATA){
	($z2name,$z2con)=split(/<>/);
	$town_name[$zc] = "$z2name";
	$town_cou[$zc] = "$z2con";
		if($zc < 53){
	$t_list .= "<option value=\"$zc\">$z2name��$cou_name[$z2con]��";
		}else{}
	$zc++;
	}




	if($in{'url'} eq ""){$nurl = "http://";}else{$nurl = "$in{'url'}";}
	if($in{'mail'} eq ""){$nmail = "\@";}else{$nmail = "$in{'mail'}";}
	if(ATTESTATION){$emes = "��<font color=red>���� ID�� ÷�ε� Ȯ�� ������ ������ ������ �ݵ�� �ùٸ��� �Է��� �ּ���.</font><BR>������ �ݵ�� �帲���� ���Ϸ� �����ֽʽÿ�. �� �ȿ´� ������ �������� �������ֽʽÿ�.";}
	print <<"EOM";
	<STYLE>BODY {
	CURSOR: url('samnet.cur')
	}
	A {
	CURSOR: url('samnet.ani'); TEXT-DECORATION: none
	}
	</STYLE>
	
	<script language="JavaScript">
		function changeImg(){
			num=document.para.chara.selectedIndex;
			document.Img.src="$IMG/"+ num +".gif";
		}
	</script>
<body bgcolor="white" text="black" link="blue" vlink="purple" alink="red" leftmargin="0" marginwidth="0" topmargin="0" marginheight="0" background="$IMG/back.jpg">
<form action="$FILE_ENTRY" method="post" name=para><input type="hidden" name="mode" value="NEW_CHARA">
<table align="center" cellpadding="0" cellspacing="0" width="950">
    <tr>
        <td width="950" colspan="6">
            <p><img src="$IMG/up.gif" width="950" height="93" border="0"></p>
        </td>
    </tr>
    <tr>
        <td width="10" height="564" rowspan="12" background="$IMG/backg.gif">
            <p>&nbsp;</p>
        </td>
        <td width="929" height="44" colspan="4" background="$IMG/backg.gif">&nbsp;            <table align="center" border="1" width="928" bordercolor="black" bordercolordark="white" bordercolorlight="white">
                <tr>
                    <td>$mess</td>
                </tr>
            </table>
</td>
        <td width="11" height="564" rowspan="12" background="$IMG/backg.gif">
            <p>&nbsp;</p>
        </td>
    </tr>
    <tr>
        <td width="929" height="10" colspan="4" background="$IMG/backg.gif">
            <p></p>
</td>
    </tr>
    <tr>
        <td width="929" height="75" colspan="4" background="$IMG/backg.gif">
            <table align="center" border="1" width="928" bordercolor="black" bordercolordark="white" bordercolorlight="white">
                <tr>
                    <td width="918" height="130">
<IFRAME WIDTH="918" HEIGHT="130" FRAMEBORDER="no" SCROLLING="yes" SRC="../sam/license.html" MARGINWIDTH="0" MARGINHEIGHT="0" NAME="ya" HSPACE="0" VSPACE="0" ></IFRAME>
</tr>
<tr>
<td>
<center><input type="checkbox" name="license" value="1"> �� ĥ�������� ����� �����մϴ�.
</td>
                </tr>
            </table>
        </td>
    </tr>
    <tr>
        <td width="929" height="10" colspan="4" background="$IMG/backg.gif">
            <p align="center"></p>
        </td>
    </tr>
    <tr>
        <td width="100" height="45" background="$IMG/backg.gif">
            <table align="center" border="1">
                <tr>
                    <td width="90" height="94">
                        <p align="center"><span style="font-size:9pt;"><font face="����" color="white">�� 
                        �� �� ��<br>&<br>�� �� ��</font></span></p>
                    </td>
                </tr>
            </table>
        </td>
        <td width="364" height="45" background="$IMG/backg.gif">
            <table align="center" border="1" width="364">
                <tr>
                    <td width="83" height="84" align="center" rowspan="2">
<TABLE><TR><TD><img src=\"$IMG/0.gif\" name=\"Img\">
</TD></TR></TABLE>                    </td>
                    <td width="265" height="62">
                        <table align="center" cellpadding="0" cellspacing="0">
                            <tr>
                                <td width="254" height="34" colspan="2"><p align="center"><select name=chara onChange=\"changeImg()\" size="1" style="font-family:�ü�; color:rgb(255,153,0); background-color:rgb(41,60,66);">
EOM
	foreach (0..$CHARA_IMAGE){
	print "<option value=\"$_\">$hi[$_]\n";
	}
	print <<"EOM";
</select></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="124">
                                    <p align="left"><span style="font-size:9pt;"><font color="white"><b>ID:<input type="text" name="id" size="10" value="$in{'id'}" style="color:rgb(255,153,0); background-color:rgb(41,60,66);"></b></font></span></p>
                                </td>
                                <td width="124">
                                    <p align="left"><span style="font-size:9pt;"><font color="white"><b>PW:<input type="password" name="pass" size="10"  value="$in{'pass'}" style="color:rgb(255,153,0); background-color:rgb(41,60,66);"></b></font></span></p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td width="265" height="20">
                        <p align="center"><font color="white"><span style="font-size:9pt;"><b>����� 
                        ������ �ֽʽÿ�.(�ߺ� �Ұ�)</b></span></font></p>
                    </td>
                </tr>
            </table>
        </td>
        <td width="100" height="45" background="$IMG/backg.gif">
            <table align="center" border="1">
                <tr>
                    <td width="90" height="94">
                        <p align="center"><span style="font-size:9pt;"><font face="����" color="white">�� �� �� ġ</font></span></p>
                    </td>
                </tr>
            </table>
        </td>
        <td width="365" height="45" background="$IMG/backg.gif">
            <table align="center" border="1" width="364">
                <tr>
                    <td width="354" height="72">
            <p align="center"><select name="con" size="1" style="font-family:�ü�; color:rgb(255,153,0); background-color:rgb(41,60,66);">
<option value=""> �������ּ���.
$t_list
</select></p>
                    </td>
                </tr>
                <tr>
                    <td width="354" height="20">
                        <p align="center"><span style="font-size:9pt;"><font face="����" color="white"><b>ĳ������ ������ �������ּ���.(������ �Ǳ�����</b>)</font></span></p>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
    <tr>
        <td width="929" background="$IMG/backg.gif" colspan="4">
            <p align="center"></p>
        </td>
    </tr>
    <tr>
        <td width="929" height="10" background="$IMG/backg.gif" colspan="4">
            <p align="center"></p>
        </td>
    </tr>
    <tr>
        <td width="100" height="85" background="$IMG/backg.gif">
            <table align="center" border="1">
                <tr>
                    <td width="90" height="84">
                        <p align="center"><span style="font-size:9pt;"><font face="����" color="white">�� 
                        �� �� ��</font></span></p>
                    </td>
                </tr>
            </table>
        </td>
        <td width="364" height="85" background="$IMG/backg.gif">
            <table align="center" border="1" width="364">
                <tr>
                    <td width="354" height="62">
                        <p align="left">	<span style="font-size:9pt;"><font color="white"><input type="radio" name="type" value="9">���Ÿ�� (�ɷ�ġ�� ��ü�� ������Դϴ�.)<br>
	<input type="radio" name="type" value="1">����Ÿ�� (����, ����� ��ü�� �����ϴ�.)<br>
	<input type="radio" name="type" value="2">����Ÿ�� (����, �ŷ��� ��ü�� �����ϴ�.)<br>
	 </font></span></p>
                    </td>
                </tr>
                <tr>
                    <td width="354" height="17">
                        <p align="center">	<span style="font-size:9pt;"><font color="white"><b>����� Ÿ���� �������ֽʽÿ�.</b></font></span></p>
                    </td>
                </tr>
            </table>
        </td>
        <td width="100" height="85" background="$IMG/backg.gif">
            <table align="center" border="1">
                <tr>
                    <td width="90" height="84">
                        <p align="center"><span style="font-size:9pt;"><font face="����" color="white">�� 
                        �� �� ��</font></span></p>
                    </td>
                </tr>
            </table>
        </td>
        <td width="365" height="85" background="$IMG/backg.gif">
            <table align="center" border="1" width="364">
                <tr>
                    <td width="354" height="62">
                        <p align="center"><input type="text" name="mail" size="30" value="$nmail" style="color:rgb(255,153,0); background-color:rgb(41,60,66);"></p>
                    </td>
                </tr>
                <tr>
                    <td width="354" height="20">
                        <p align="center"><span style="font-size:9pt;"><font face="����" color="white"><b>���������� ���� �����ּҸ� �����ֽʽÿ�.</b></font></span></p>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
    <tr>
        <td width="929" height="10" background="$IMG/backg.gif" colspan="4">
            <p></p>
        </td>
    </tr>
    <tr>
        <td width="100" height="67" background="$IMG/backg.gif">
            <table align="center" border="1">
                <tr>
                    <td width="90" height="96">
                        <p align="center"><span style="font-size:9pt;"><font face="����" color="white"><input type="radio" name="gunju" value="1">�� 
                        �� �� ��</font></span></p>
                    </td>
                </tr>
            </table>
        </td>
        <td width="829" height="67" background="$IMG/backg.gif" colspan="3">
            <table align="center" border="1" width="827" bordercolor="black" bordercolordark="white" bordercolorlight="white">
                <tr>
                    <td width="817" height="62">
                        <p align="center"><span style="font-size:9pt;"><font face="����"><input type="radio" name="cou_name1" value="1"></font></span><font color=#00A5FF face="����"><span style="font-size:9pt;">������(��) 
                        <input type="radio" name="cou_name1" value="2"></span><font color="#33CC66" face="����"><span style="font-size:9pt;">�˳���(��)</span><font color=#00A5FF face="����"><font color=#006400><span style="font-size:9pt;"> 
                        <input type="radio" name="cou_name1" value="3"></span><font color="#FF7897" face="����"><span style="font-size:9pt;">������(��)</span><font color=#00A5FF face="����"><font color=#006400><font color=#B9062F><span style="font-size:9pt;"><input type="radio" name="cou_name1" value="4"></span></font><font color="#9966CC" face="����"><span style="font-size:9pt;">�ʳ���(��)</span><font color=#00A5FF face="����"><font color=#006400><font color=#B9062F><font color=#800080><span style="font-size:9pt;"><input type="radio" name="cou_name1" value="5"></span></font></font><font color="#CCCCCC" face="����"><span style="font-size:9pt;">������(��)</span><font color=#00A5FF face="����"><font color=#006400><font color=#B9062F><font color=#800080><font color=#282828><span style="font-size:9pt;"><input type="radio" name="cou_name1" value="6"></span><font color=#D2691E><span style="font-size:9pt;">�ѳ���(��)<input type="radio" name="cou_name1" value="7"></span></font></font></font></font><font color="#A57451" face="����"><span style="font-size:9pt;">����(��)</span><input type="radio" name="cou_name1" value="8"></span><font color="#EEE12F" face="����"><span style="font-size:9pt;">�Ŷ�(��)</span><input type="radio" name="cou_name1" value="9"></span><font color="#009999" face="����"><span style="font-size:9pt;">����(��)</span></td>
                </tr>
                <tr>
                    <td width="817" height="20">
                        <p align="center"><span style="font-size:9pt;"><font color="white" face="����">���ַ� �Ͻ� ���� <font color=red>���� ���� ��ư</font>�� üũ�� �� ������ �������ֽʽÿ�. �� �̹� �Ǳ��� ����� �Ǳ��� �� �����ϴ�.<br>������ư�� üũ�� ���� �ʰ� ����ϰ� �Ǹ� ����λ�� �����ϰ� �˴ϴ�.</font></span></p>
</td>
                </tr>
            </table>
        </td>
    </tr>
    <tr>
        <td width="929" height="10" background="$IMG/backg.gif" colspan="4">
            <p>&nbsp;</p>
        </td>
    </tr>
    <tr>
        <td width="929" height="68" background="$IMG/backg.gif" colspan="4">
            <p align="center"><input type="submit" style="font-family:�ü�; color:rgb(255,153,0); background-color:rgb(41,60,66); border-style:none;" value="�ﱹ�� �������� NET ���"></form>        </td>
    </tr>
    <tr>
        <td width="950" height="28" colspan="6">
            <p><img src="$IMG/down.gif" width="950" height="26" border="0"></p>
        </td>
    </tr>
</table>


EOM

	
	&FOOTER;

	exit;
}

sub CHEACKER {

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR2("���� ���� ����");
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
			&ERR2("�ִ� ��ϼ� [$ENTRY_MAX]�� �Ѱ� �ֽ��ϴ�. ���� �ű� ����� ���� �����ϴ�.");
		}
	}
}
1;