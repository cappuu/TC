
sub MINSIM{
						$ksub2=0;
						if($krice<100){
							&K_LOG("$mmonth�� : ���� ������ ������ �� �������ϴ�.");
						}elsif($zpri >= 100){
							&K_LOG("$mmonth�� : �ν��� ���̻� �ø� �� �����ϴ�.");
							$zpri=100;
						}else{
							if($kskill =~ /Fa/){
							$zpriadd = int(int($kchat)/20 + rand(int($kchat)) / 15);
							}else{
							$zpriadd = int(int($kchat)/20 + rand(int($kchat)) / 20);
							}
							$zpri += $zpriadd;
							$krice -= 100;
							$kcex += 30;
							$kexp += 30;
							$kpoint += 10;
							if($zpri > 100){
								$zpri=100;
							}


							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($kcodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /�ν�/){
										if($qup =~ /�ν�/){
										$kqpoint += $zpriadd;
										}else{
										$kqpoint += $qup;
										}
										if($qtalkd eq ""){
										}else{
										&K_LOG("$mmonth�� : $qtalkd");
										}
									}	
								}
							}

							if($kcodea =~ /C6/ && 30 > rand(100)){
								if($kintt > rand(200)){
								$kqpoint += 1;
								&K_LOG("$mmonth�� : [��ȭ��] ��ũ~ ���״�!");
								&K_LOG("$mmonth�� : ���� �������� �õ��ϴ� ��ȭ���� ��Ҵ�!");
								}else{
								&K_LOG("$mmonth�� : ��ȭ���� ���� ��� �ܼ��� ã�� ���� ������.");
								}
							}

							if($kcodea =~ /B5/){
							$kqpoint += $zpriadd;
							}

							if("$zname" ne ""){
								splice(@TOWN_DATA,$kpos,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");
							}

							&K_LOG("$mmonth�� : $zname���� �ν��� <font color=red>+$zpriadd</font> �ö����ϴ�.");
							$kcha_ex++;
							$go_ex += int($kbank/5);
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
						}
}
1;

