
sub IMGWAN{
						$ksub2=0;
						&CON_NUM;
						&COUNTRY_DATA_OPEN($kcon);


						$timelimit = $F_YEAR+$myear;

						if($xcid eq 0){
							if($cou_name[$cnum] eq ""){
								&K_LOG("$mmonth�� : �� ���� ���� �� �����ϴ�.");
							}elsif($timelimit < 184 && $connum1 >= 20){
								&K_LOG("$mmonth�� : 184�� 1�� �������� $cou_name[$cnum]���� �Ӱ��� �� �����ϴ�.");
							}else{
								if(@B_LIST eq "0"){
									open(IN,"./log_file/black_list.cgi");
									@B_LIST = <IN>;
									close(IN);
								}
								$b_hit=0;
								foreach(@B_LIST){
									($bid,$bcon,$bname,$bsub) = split(/<>/);
									if($bid eq $kid && $bcon eq $kcon){
										$b_hit=1;
									}
								}
								if($b_hit){
									&K_LOG("$mmonth�� : $cou_name[$cnum]������ �Ӱ��� �źεǾ����ϴ�.");
								}else{	
				
									$kcon = $cnum;
									&K_LOG("$mmonth�� : $cou_name[$cnum]�� �Ӱ��߽��ϴ�.");
									&HISTORY_LOG($kid,"$cou_name[$cnum]�� �Ӱ��߽��ϴ�.");
									&MAP_LOG("<img src=$IMG/j2.gif> $kname���� $cou_name[$cnum]������ �Ӱ��߽��ϴ�.");
								}
							}
						}else{
							&K_LOG("$mmonth�� : ��߰� �ƴϸ� ���� ���� �����ϴ�.");
						}
}
1;

