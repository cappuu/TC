
sub ILGITO{



							open(IN,"./charalog/main/$cnum\.cgi");
							@E_DATA = <IN>;
							close(IN);
							($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/,$E_DATA[0]);
							($estr_ex,$eint_ex,$elea_ex,$echa_ex,$esub1_ex,$esub2_ex,$ebo_ex,$egi_ex,$ech_ex,$egu_ex,$ego_ex,$ejin_ex) = split(/,/,$esub1);

							if($kpos != $epos){
							&K_LOG("$mmonth�� : ����� ���� ��ġ�� ���� �ʽ��ϴ�.");
							}else{
							
										&CHARA_ITEM_OPEN;

										$kche = 100;
										$eche = 100;

										if($csub == 1){
										&K_LOG4("\[$old_date\]$ename(����:$estrt ���:$eleat)�԰� �ϱ��並 ����!");
										&E_LOG4("\[$old_date\]$kname(����:$kstrt ���:$kleat)�԰� �ϱ��並 ����!");



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

										if($kcodea =~ /B8/){
											if(119 < $estr+$elea){
											$kqpoint += 1;
											&K_LOG("$mmonth�� : [$kname]: ����, $ename�� ���� �ϱ��信�� �¸��߱�. ���������?��");
											}else{
											&K_LOG("$mmonth�� : [$kname]: ����, ���д�. �ɷ�ġ�� �ʹ� ���� ��븦 �����.��");
											}
										}

							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($kcodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /�ϱ���/){
										$kqpoint += $qup;
										if($qtalkd eq ""){
										}else{
										&K_LOG("$mmonth�� : $qtalkd");
										}
									}	
								}
							}


										&MAP_LOG("<img src=$IMG/j25.gif> $kname���� $ename���� ���� �ϱ��信�� �¸�!");
										&K_LOG4("\[$old_date\]$kname���� $ename���� ���� �ϱ��信�� �¸�!");
										&E_LOG4("\[$old_date\]$kname���� $ename���� ���� �ϱ��信�� �¸�!");
										}else{
										&MAP_LOG("<img src=$IMG/j25.gif> $ename���� $kname���� ���� �ϱ��信�� �¸�!");
										&K_LOG4("\[$old_date\]$ename���� $kname���� ���� �ϱ��信�� �¸�!");
										&E_LOG4("\[$old_date\]$ename���� $kname���� ���� �ϱ��信�� �¸�!");
										}

										}elsif($csub == 2){
										&K_LOG4("\[$old_date\]$ename(����:$eintt �ŷ�:$echat)�԰� ������ ����!");
										&E_LOG4("\[$old_date\]$kname(����:$kintt �ŷ�:$kchat)�԰� ������ ����!");
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
											$wine = 1;
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
										&K_LOG4("<font color=red>$count</font>ȸ:$kname�� ���ŷ�($kstrt) $kche (-$edmge\) VS $ename�� ���ŷ�($estrt) $eche (-$kdmge\)");
										}

										if($wine){
										if($kcodea =~ /B8/){
											if(149 < $eint+$echa){
											$kqpoint += 1;
											&K_LOG("$mmonth�� : [$kname]: ����, $ename�� ���� �������� �¸��߱�. ���������?��");
											}else{
											&K_LOG("$mmonth�� : [$kname]: ����, ���д�. �ɷ�ġ�� �ʹ� ���� ��븦 �����.��");
											}
										}

							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($kcodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /����/){
										$kqpoint += $qup;
										if($qtalkd eq ""){
										}else{
										&K_LOG("$mmonth�� : $qtalkd");
										}
									}	
								}
							}


										&MAP_LOG("<img src=$IMG/j26.gif> $kname���� $ename���� ���� �������� �¸�!");
										&K_LOG4("\[$old_date\]$kname���� $ename���� ���� �������� �¸�!");
										&E_LOG4("\[$old_date\]$kname���� $ename���� ���� �������� �¸�!");
										}elsif(!$wine){
										&MAP_LOG("<img src=$IMG/j26.gif> $ename���� $kname���� ���� �������� �¸�!");
										&K_LOG4("\[$old_date\]$ename���� $kname���� ���� �������� �¸�!");
										&E_LOG4("\[$old_date\]$ename���� $kname���� ���� �������� �¸�!");
										}


							}
						}	
}
1;

