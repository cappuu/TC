
sub JINGBYUNG{
						$ksub2=0;

						if($kcha > 40){
						$ga = int($kchat/5);
						}
						if($kgold < $ggyo){
							&K_LOG("$mmonth�� : [����] : �������� ������� �ʽ��ϴ�.");

						}elsif($znum < $cnum){
							&K_LOG("$mmonth�� : [����] : ��ε��� ������� �ʽ��ϴ�.");
						}elsif($cnum <= 0){
							&K_LOG("$mmonth�� : [����] : ���縦 0�� ���Ϸ� ¡���� �� �����ϴ�.");
						}elsif($zpri < int($cnum / 300)){
							&K_LOG("$mmonth�� ; [����] : ��ε��� �ź��߽��ϴ�.");
						}elsif($znum < 0){
							&K_LOG("$mmonth�� ; [����] : ��ε��� 0 ���Ϸ� ������ �� �����ϴ�.");
							$znum = 0;
						}elsif($kskill =~ /Ac/){

						if($ggyo < 10){$ggyo=int(($cnum * 10)/30);}
							if($ksub1_ex == $csub){
								if($ksol + $cnum > ($kleat)*30){
									$cnum = int(($kleat)*30) - $ksol;
								}
								$ksol += $cnum;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
							}else{
								if($cnum > ($kleat)*30){
									$cnum = $kleat*30;
								}
								$ksol = $cnum;
							}
							$kgat -= int($cnum/30);
							if($kgat < 0 ){
								$kgat = 0;
							}
							$ksub1_ex = $csub;
							$kcex += 10;
							$kexp += 10;
							$kpoint += 4;

						if($kskill =~ /Bc/ && $csub == 7){
						$ggyo = int($cnum * ($SOL_PRICE[$csub] - $ga)/60);
						}elsif($kskill =~ /Cc/ && $csub == 12){
						$ggyo = int($cnum * ($SOL_PRICE[$csub] - $ga)/40);
						}else{
						$ggyo = int($cnum * ($SOL_PRICE[$csub] - $ga)/30);
						}



							$kgold -= $ggyo;




							if($kskill =~ /Db/ && $zpri >= 75){
							}else{
							$znum -= $cnum;
							}

							$zpri -= int($cnum / 300);
							if("$zname" ne ""){
								splice(@TOWN_DATA,$kpos,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");
							}

							&K_LOG("$mmonth�� : $SOL_TYPE[$ksub1_ex]�� <font color=red>+$cnum</font> ¡���߽��ϴ�. [¡���ݾ� : $ggyo]");
							if($cnum > 14){
							$kstr_ex++;
							$go_ex += int($kbank/5);
							}
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
						}elsif("7" eq $csub && $zsub1 < 1150){
							&K_LOG("$mmonth�� : [����] : Ȳ�Ǳ������� �����ϱ⿡�� ������� �����մϴ�.");
						}elsif("15" eq $csub && $zsub1 < 899){
							&K_LOG("$mmonth�� : [����] : ������� �����ϱ⿡�� ������� �����մϴ�.");
						}elsif("8" eq $csub && $zsub1 < 750){
							&K_LOG("$mmonth�� : [����] : �ڳ������� �����ϱ⿡�� ������� �����մϴ�.");
						}elsif("9" eq $csub && $zsub1 < 1150){
							&K_LOG("$mmonth�� : [����] : ��Ǻ��� �����ϱ⿡�� ������� �����մϴ�.");
						}elsif("10" eq $csub && $zsub1 < 1100){
							&K_LOG("$mmonth�� : [����] : ö�⺴�� �����ϱ⿡�� ������� �����մϴ�.");
						}elsif("11" eq $csub && $zsub1 < 1100){
							&K_LOG("$mmonth�� : [����] : ȭ���� �����ϱ⿡�� ������� �����մϴ�.");
						}elsif("1" eq $csub && $zsub1 < 100){
							&K_LOG("$mmonth�� : [����] : �ú��� �����ϱ⿡�� ������� �����մϴ�.");
						}elsif("2" eq $csub && $zsub1 < 250){
							&K_LOG("$mmonth�� : [����] : â���� �����ϱ⿡�� ������� �����մϴ�.");
						}elsif("3" eq $csub && $zsub1 < 450){
							&K_LOG("$mmonth�� : [����] : ���庸���� �����ϱ⿡�� ������� �����մϴ�.");
						}elsif("4" eq $csub && $zsub1 < 750){
							&K_LOG("$mmonth�� : [����] : �⺴�� �����ϱ⿡�� ������� �����մϴ�.");
						}elsif("6" eq $csub && $zsub1 < 800){
							&K_LOG("$mmonth�� : [����] : �Ǻ��� �����ϱ⿡�� ������� �����մϴ�.");
						}elsif("7" eq $csub && ($zname eq "����" || $zname eq "����" || $zname eq "�ǳ�" || $zname eq "����" || $zname eq "����" || $zname eq "�˰�" || $zname eq "�ڵ�" || $zname eq "����" || $zname eq "����" || $zname eq "ȫ��" || $zname eq "��" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "�ž�" || $zname eq "����" || $zname eq "���" || $zname eq "���" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "�û�" || $zname eq "���" || $zname eq "����" || $zname eq "��" || $zname eq "����" || $zname eq "�ܾ�" || $zname eq "����" || $zname eq "��" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "�Ϻ�" || $zname eq "����" || $zname eq "��" || $zname eq "ȸ��" || $zname eq "����" || $zname eq "����" || $zname eq "���" || $zname eq "�ż�" || $zname eq "�����" || $zname eq "�" || $zname eq "õ��" || $zname eq "����")){
							&K_LOG("$mmonth�� : [����] : �ش� ���������� Ȳ�Ǳ������� ���� ���� �����ϴ�..");
						}elsif("5" eq $csub && $zsub1 < 1000){
							&K_LOG("$mmonth�� : [����] : �űͺ��� �����ϱ⿡�� ������� �����մϴ�.");
						}elsif("8" eq $csub && ($zname eq "����" || $zname eq "���" || $zname eq "���" || $zname eq "����" || $zname eq "��" || $zname eq "��â" || $zname eq "�Ǿ�" || $zname eq "��" || $zname eq "����" || $zname eq "�ǳ�" || $zname eq "�ڵ�" || $zname eq "����" || $zname eq "����" || $zname eq "ȫ��" || $zname eq "��" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "�ž�" || $zname eq "����" || $zname eq "���" || $zname eq "���" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "�û�" || $zname eq "���" || $zname eq "����" || $zname eq "��" || $zname eq "����" || $zname eq "�ܾ�" || $zname eq "����" || $zname eq "��" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "�Ϻ�" || $zname eq "����" || $zname eq "��" || $zname eq "ȸ��" || $zname eq "����" || $zname eq "����" || $zname eq "���" || $zname eq "�ż�" || $zname eq "�����" || $zname eq "õ��" || $zname eq "����")){
							&K_LOG("$mmonth�� : [����] : �ش� ���������� �ڳ������� ���� ���� �����ϴ�..");
						}elsif("9" eq $csub && ($zname eq "���" || $zname eq "���" || $zname eq "����" || $zname eq "��" || $zname eq "��â" || $zname eq "�Ǿ�" || $zname eq "��" || $zname eq "ȫ��" || $zname eq "��" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "�ž�" || $zname eq "����" || $zname eq "���" || $zname eq "���" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "�û�" || $zname eq "���" || $zname eq "����" || $zname eq "��" || $zname eq "����" || $zname eq "�ܾ�" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "�Ϻ�" || $zname eq "����" || $zname eq "��" || $zname eq "ȸ��" || $zname eq "���" || $zname eq "�ż�" || $zname eq "õ��" || $zname eq "�")){
							&K_LOG("$mmonth�� : [����] : �ش� ���������� ��Ǻ��� ���� ���� �����ϴ�..");
						}elsif("10" eq $csub && ($zname eq "���" || $zname eq "���" || $zname eq "����" || $zname eq "��" || $zname eq "��â" || $zname eq "�Ǿ�" || $zname eq "��" || $zname eq "ȫ��" || $zname eq "��" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "�ž�" || $zname eq "����" || $zname eq "���" || $zname eq "���" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "�û�" || $zname eq "���" || $zname eq "����" || $zname eq "��" || $zname eq "����" || $zname eq "�ܾ�" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "�Ϻ�" || $zname eq "����" || $zname eq "��" || $zname eq "ȸ��" || $zname eq "���" || $zname eq "�ż�" || $zname eq "õ��" || $zname eq "�" || $zname eq "����")){
							&K_LOG("$mmonth�� : [����] : �ش� ���������� ö�⺴�� ���� ���� �����ϴ�..");
						}elsif("11" eq $csub && ($zname eq "����" || $zname eq "���" || $zname eq "���" || $zname eq "����" || $zname eq "��" || $zname eq "��â" || $zname eq "�Ǿ�" || $zname eq "��" || $zname eq "����" || $zname eq "�ǳ�" || $zname eq "����" || $zname eq "����" || $zname eq "�˰�" || $zname eq "�ڵ�" || $zname eq "����" || $zname eq "����" || $zname eq "ȫ��" || $zname eq "��" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "�ž�" || $zname eq "����" || $zname eq "���" || $zname eq "���" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "�û�" || $zname eq "���" || $zname eq "����" || $zname eq "��" || $zname eq "����" || $zname eq "�ܾ�" || $zname eq "����" || $zname eq "��" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "�Ϻ�" || $zname eq "����" || $zname eq "��" || $zname eq "ȸ��" || $zname eq "����" || $zname eq "����" || $zname eq "���" || $zname eq "�ż�" || $zname eq "�" || $zname eq "õ��" || $zname eq "����")){
							&K_LOG("$mmonth�� : [����] : �ش� ���������� ȭ���� ���� ���� �����ϴ�..");
						}elsif("13" eq $csub && $zsub1 < 900){
							&K_LOG("$mmonth�� ; [����] : Ȳ������ �����ϱ⿡�� ������� �����մϴ�.");
						}elsif("12" eq $csub && $zsub1 < 1199){
							&K_LOG("$mmonth�� ; [����] : �߼��Ÿ� �����ϱ⿡�� ������� �����մϴ�.");
						}elsif("17" eq $csub && $zsub1 < 1199){
							&K_LOG("$mmonth�� ; [����] : �ļ����� �����ϱ⿡�� ������� �����մϴ�.");
						}elsif("15" eq $csub && ($zname eq "����" || $zname eq "���" || $zname eq "���" || $zname eq "����" || $zname eq "��" || $zname eq "��â" || $zname eq "�Ǿ�" || $zname eq "��" || $zname eq "����" || $zname eq "�ǳ�" || $zname eq "����" || $zname eq "����" || $zname eq "�˰�" || $zname eq "�ڵ�" || $zname eq "����" || $zname eq "����" || $zname eq "ȫ��" || $zname eq "��" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "�ž�" || $zname eq "����" || $zname eq "���" || $zname eq "���" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "�û�" || $zname eq "���" || $zname eq "����" || $zname eq "��" || $zname eq "����" || $zname eq "�ܾ�" || $zname eq "����" || $zname eq "��" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "�Ϻ�" || $zname eq "����" || $zname eq "��" || $zname eq "�" || $zname eq "����" || $zname eq "����" || $zname eq "���" || $zname eq "�ż�" || $zname eq "�����" || $zname eq "õ��" || $zname eq "����")){
							&K_LOG("$mmonth�� : [����] : �ش� ���������� ������� ���� ���� �����ϴ�..");
						}elsif("16" eq $csub && $zsub1 < 499){
							&K_LOG("$mmonth�� : [����] : ��κ��� �����ϱ⿡�� ������� �����մϴ�.");
						}elsif("18" eq $csub && $zsub1 < 999){
							&K_LOG("$mmonth�� : [����] : �غ��� �����ϱ⿡�� ������� �����մϴ�.");
						}elsif("19" eq $csub && $zsub1 < 749){
							&K_LOG("$mmonth�� : [����] : ������ �����ϱ⿡�� ������� �����մϴ�.");
						}elsif("20" eq $csub && $zsub1 < 1099){
							&K_LOG("$mmonth�� : [����] : ������ �����ϱ⿡�� ������� �����մϴ�.");
						}else{


						if($ggyo < 10){$ggyo=int(($cnum * 10)/30);}
							if($ksub1_ex == $csub){
								if($ksol + $cnum > ($kleat)*30){
									$cnum = int(($kleat)*30) - $ksol;
								}
								$ksol += $cnum;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
							}else{
								if($cnum > ($kleat)*30){
									$cnum = $kleat*30;
								}
								$ksol = $cnum;
							}


							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($kcodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /¡��/){
										if($qup =~ /¡��/){
										$kqpoint += $cnum;
										}else{
										$kqpoint += $qup;
										}
										&K_LOG("$mmonth�� : $qtalkd");
									}
								}
							}


							$kgat -= int($cnum/30);
							if($kgat < 0 ){
								$kgat = 0;
							}
							$ksub1_ex = $csub;

							if($kcodea =~ /B6/ && $ksub1_ex == 6){
								$kqpoint += $cnum;
							}


							$kcex += 10;
							$kexp += 10;
							$kpoint += 4;

						if($kskill =~ /Bc/ && $csub == 7){
						$ggyo = int($cnum * ($SOL_PRICE[$csub] - $ga)/60);
						}elsif($kskill =~ /Bc/ && $kskill =~ /Fc/ && $csub == 7){
						$ggyo = int($cnum * ($SOL_PRICE[$csub] - $ga)/30);
						}elsif($kskill =~ /Fc/){
						$ggyo = int($cnum * ($SOL_PRICE[$csub] - $ga)/15);
						}else{
						$ggyo = int($cnum * ($SOL_PRICE[$csub] - $ga)/30);
						}


							$kgold -= $ggyo;




							if($kskill =~ /Db/ && $zpri >= 75){
							}else{
							$znum -= $cnum;
							}

							$zpri -= int($cnum / 300);
							if("$zname" ne ""){
								splice(@TOWN_DATA,$kpos,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");
							}

							&K_LOG("$mmonth�� : $SOL_TYPE[$ksub1_ex]�� <font color=red>+$cnum</font> ¡���߽��ϴ�. [¡���ݾ� : $ggyo]");
							if($cnum > 14){
							$kstr_ex++;
							$go_ex += int($kbank/5);
							}
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
						}
}
1;
