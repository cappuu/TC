
sub JANGBI{
						$ksub2=0;						open(IN,"$ARM_LIST");
						@ARM_DATA = <IN>;
						close(IN);
						($armname,$armval,$armdmg,$armwei,$armele,$armsta,$armclass,$armtownid) = split(/<>/,$ARM_DATA[$cnum]);						($armname2,$armval2) = split(/<>/,$ARM_DATA[$karm]);
						$armval2 = int($armval2 * 0.6);
						if($armval > $kgold + $armval2){
							&K_LOG("$mmonth�� : $armname�� ��⿡�� �������� ������� �ʽ��ϴ�.(�� : $armval)");
						}else{
							if($kcodea =~ /B8/){
							$kqpoint = 1;
							}
							$kgold += $armval2;
							$kgold -= $armval;
							$karm = $cnum;
							&K_LOG("$mmonth�� : ��� : $armname2�� �� <font color=red>$armval2</font>�� �Ⱦ� $armname�� �����߽��ϴ�.");
							&MAP_LOG("<img src=$IMG/j22.gif> $kname���� $armname�� �����߽��ϴ�.");
							&HISTORY_LOG($kid,"$armname�� �����߽��ϴ�.");
						}
}
1;

