sub SKILL_BUY {

	if($in{'no'} eq ""){&ERR("NO:�� �Էµ��� �ʽ��ϴ�.");}
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&TIME_DATA;
	open(IN,"$SKILL_LIST");
	@SKILL_DATA = <IN>;
	close(IN);
	&HEADER;
	$no = $in{'no'} + 1;

	foreach(@no){
		$no_list .= "<input type=hidden name=no value=$_>"
	}

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
<table align="center" cellpadding="0" cellspacing="0" width="945">
    <tr>
        <td width="945">
            <p><img src="$IMG/up.gif" width="950" height="93" border="0"></p>
        </td>
    </tr>
    <tr>
        <td width="945" height="545" background="$IMG/backg.gif">
            <table align="center" cellpadding="0" cellspacing="0" width="749" bordercolordark="white" bordercolorlight="black">
                <tr>
                    <td width="749" height="11" colspan="14">
                    </td>
                </tr>
                <tr>
                    <td width="749" height="60" colspan="14" bgcolor="black">
                        <p><span style="font-size:9pt;"><b>Ư�ⱳ����</b><br>Ư������Ʈ�� �̿��Ͽ� 
                        �� ������ Ư�⸦ ��� �� �ֽ��ϴ�.<br>���� $kname�Բ����� 
                        <font color="red"><b>$kpoint Ư������Ʈ</b></font>�� ������ ��ʴϴ�<br>�ش� Ư�� �̹����� 
                        ���콺�� ���ٴ�� Ư�⿡ ���� �ڼ��� ������ �� �� �ֽ��ϴ�.</span></p>
                    </td>
                </tr>
                <tr>
                    <td width="749" height="8" colspan="14">
                    </td>
                </tr>
                <tr>
                    <td width="92" height="97">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p align="center"><img src="$IMG/skill1a.jpg" width="80" height="80" border="0" alt="���ġ�� ���� ��½�Ų��.
����Ʈ:1000"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="0">
<input type=hidden name=mode value=56>
<input type=submit value="  ����  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="10" height="522" rowspan="5">
                    </td>
                    <td width="92" height="97">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill2a.jpg" width="80" height="80" border="0" alt="���ġ�� ���� ��½�Ų��.
����Ʈ:1000"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="3">
<input type=hidden name=mode value=56>
<input type=submit value="  ����  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="10" height="522" rowspan="5">
                    </td>
                    <td width="92" height="97">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill3a.jpg" width="80" height="80" border="0" alt="���ġ�� ���� ��½�Ų��.
����Ʈ:1000"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="6">
<input type=hidden name=mode value=56>
<input type=submit value="  ����  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="10" height="522" rowspan="5">
                    </td>
                    <td width="92" height="97">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill4a.jpg" width="80" height="80" border="0" alt="�����缺�� ���� ��½�Ų��.
����Ʈ:1000"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="9">
<input type=hidden name=mode value=56>
<input type=submit value="  ����  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="10" height="522" rowspan="5">
                    </td>
                    <td width="92" height="154">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill5a.jpg" width="80" height="80" border="0" alt="������ �Ʒ��̳� ���Ʒý� �Ʒõ��� ��½�Ų��.
����Ʈ:1000"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="12">
<input type=hidden name=mode value=56>
<input type=submit value="  ����  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="10" height="522" rowspan="5">
                    </td>
                    <td width="92" height="154">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill6at.jpg" width="80" height="80" border="0" alt="�ν��� ��½�Ų��.
����Ʈ:1000"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="15">
<input type=hidden name=mode value=56>
<input type=submit value="  ����  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="10" height="522" rowspan="5">
                        <p>&nbsp;</p>
                    </td>
                    <td width="91" height="154">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill7a.jpg" width="80" height="80" border="0" alt="������ �Ʒû��ѵ��� 120���� �ø���.
����Ʈ:1000"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="18">
<input type=hidden name=mode value=56>
<input type=submit value="  ����  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="46" height="522" rowspan="5">
                        <p>&nbsp;</p>
                    </td>
                </tr>
                <tr>
                    <td width="92" height="30">
                        <p align="center">��</p>
                    </td>
                    <td width="92" height="30">
                        <p align="center">��</p>
                    </td>
                    <td width="92" height="30">
                        <p align="center">��</p>
                    </td>
                    <td width="92" height="30">
                        <p align="center">��</p>
                    </td>
                    <td width="92" height="30">
                        <p align="center">��</p>
                    </td>
                    <td width="92" height="30">
                        <p align="center">��</p>
                    </td>
                    <td width="91" height="30">
                        <p align="center">��</p>
                    </td>
                </tr>
                <tr>
                    <td width="92" height="103">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill1bt.jpg" width="80" height="80" border="0" alt="[Ư�����ʼ�]
�ŷ������� 5000���� ��½�Ű�� �۱� ������ 10000���� �þ��.
����Ʈ:1850"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value=1>
<input type=hidden name=mode value=56>
<input type=submit value="  ����  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="92" height="103">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill2b.jpg" width="80" height="80" border="0" alt="[Ư�����ʼ�]
��ǰ�ŷ��� �� ��ΰ� �Ǵ�.
����Ʈ:2000"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="4">
<input type=hidden name=mode value=56>
<input type=submit value="  ����  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="92" height="103">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill3b.jpg" width="80" height="80" border="0" alt="[Ư�����ʼ�]
������ 100% Ȯ���� ���Ѵ�.
����Ʈ:2000"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="7">
<input type=hidden name=mode value=56>
<input type=submit value="  ����  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="92" height="103">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill4b.jpg" width="80" height="80" border="0" alt="[Ư��缺�ʼ�]
¡���� �ص� ����� ���� �ʴ´�.
¡���� �ʿ��� �ּҳ���� �־�� �ϰ� ���� �ν��� 75�̻��̾�� �Ѵ�.
����Ʈ:2000"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="10">
<input type=hidden name=mode value=56>
<input type=submit value="  ����  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="92" height="154">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill5b.jpg" width="80" height="80" border="0" alt="[Ư���Ʒ��ʼ�]
�������� ����,�ú�,â��,���庸���� ���ݷ�,������� +20�Ѵ�.
����Ʈ:2000"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="13">
<input type=hidden name=mode value=56>
<input type=submit value="  ����  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="92" height="154">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill6b.jpg" width="80" height="80" border="0" alt="[Ư��ν��ʼ�]
Ȳ������ ����¿� �ŷ��� �����Ѵ�.
����Ʈ:1800"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="16">
<input type=hidden name=mode value=56>
<input type=submit value="  ����  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="91" height="154">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill7b.jpg" width="80" height="80" border="0" alt="[Ư�����ʼ�]
�ڽ��� ��������Ʈ�� 20% ����Ѵ�.
����Ʈ:1950"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="19">
<input type=hidden name=mode value=56>
<input type=submit value="  ����  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td width="92" height="30">
                        <p align="center">��</p>
                    </td>
                    <td width="92" height="30">
                        <p align="center">��</p>
                    </td>
                    <td width="92" height="30">
                        <p align="center">��</p>
                    </td>
                    <td width="92" height="30">
                        <p align="center">��</p>
                    </td>
                    <td width="92" height="30">
                        <p align="center">��</p>
                    </td>
                    <td width="92" height="30">
                        <p align="center">��</p>
                    </td>
                    <td width="92" height="30">
                        <p align="center">��</p>
                    </td>
                </tr>
                <tr>
                    <td width="92" height="107">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill1c.jpg" width="80" height="80" border="0" alt="[Ư��ŷ��ʼ�]
��� ���������� ���ġ�� ������� �ʰ� ���ϴ� ������ ¡�������ϴ�.
����Ʈ:3200"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="2">
<input type=hidden name=mode value=56>
<input type=submit value="  ����  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="92" height="107">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill2c.jpg" width="80" height="80" border="0" alt="[Ư������ʼ�]
���� 'Ȳ�Ǳ�����'�� ������ 50% �ٿ��Ų��.
����Ʈ:2500"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="5">
<input type=hidden name=mode value=56>
<input type=submit value="  ����  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="92" height="107">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill3c.jpg" width="80" height="80" border="0" alt="[Ư��ȸ���ʼ�]
�߼����� �����ݷ¿� ������ ����ȴ�.
����Ʈ:2300"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="8">
<input type=hidden name=mode value=56>
<input type=submit value="  ����  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="92" height="107">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill4c.jpg" width="80" height="80" border="0" alt="[Ư����ʼ�]
������ġ�� ������ 2��� ����ϰ� ������ġ�� ����ġ 2�谡 �ȴ�.
����Ʈ:2500"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="11">
<input type=hidden name=mode value=56>
<input type=submit value="  ����  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="92" height="154">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill5c.jpg" width="80" height="80" border="0" alt="[Ư�⵶���ʼ�]
�ڱ��� ���� �ƴ� Ÿ���� �������� �⺴�� �����ϴ�.
����Ʈ:3500"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="14">
<input type=hidden name=mode value=56>
<input type=submit value="  ����  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="92" height="154">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill6c.jpg" width="80" height="80" border="0" alt="[Ư��ŷ��ʼ�]
�ŷ��� ���¿� �����Ѵ�.
��, ��� ������ ������ 2�谡 �ȴ�.
����Ʈ:3200"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="17">
<input type=hidden name=mode value=56>
<input type=submit value="  ����  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="91" height="154">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill7c.jpg" width="80" height="80" border="0" alt="[Ư�⺴���ʼ�]
���ݽ� �ϱ��䰡 �ߵ��Ǹ� 50%�� Ȯ����
�� 1�տ� ������ �¸��Ͽ� �ڽ��� ���¸�ŭ�� �Ƿε��� �߰��ϰ� ���ظ� �� ��ġ��ŭ �߰� SP�� �޴´�.
����Ʈ:3300"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="20">
<input type=hidden name=mode value=56>
<input type=submit value="  ����  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td width="749" height="34" colspan="14">

                    </td>
                </tr>
                <tr>
		<form action="$FILE_STATUS" method="post">
                    <td width="749" height="45" colspan="14" bgcolor="black">
                            <p align="center"><input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="�޴��� ���ƿ´�">
                    </td>
		    </form>
                </tr>
                <tr>
                    <td width="749" height="18" colspan="14">
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
1;