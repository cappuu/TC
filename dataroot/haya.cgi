
sub HAYA{
					if($kcon eq "0"){
					&K_LOG("$mmonth�� : �̹� �ϾߵǾ����ϴ�.");
					}else{

		open(IN,"$DEF_LIST");
		@DEF_LIST3 = <IN>;
		close(IN);

							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($kcodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /�Ͼ�/){
										$kqpoint += $qup;
										if($qtalkd eq ""){
										}else{
										&K_LOG("$mmonth�� : $qtalkd");
										}
									}	
								}
							}


		@NEW_DEF_LIST3=();
		foreach(@DEF_LIST3){
		($did,$dname,$dtown_id,$dtown_flg,$dcon,$dchara,$dsol,$dsub1_ex,$dtown_battle,$ddef) = split(/<>/);
		if("$kid" ne "$did"){
			push(@NEW_DEF_LIST3,"$_");
			}
		}
		open(OUT,">$DEF_LIST");
		print OUT @NEW_DEF_LIST3;
		close(OUT);

					&BONG_DEL;
					$kcon = 0;
					&K_LOG("$mmonth�� : ������ ������ ����λ�� �Ͼ��߽��ϴ�.");
					$kcex = 0;
					$ksol = 0;
					}
}
1;

