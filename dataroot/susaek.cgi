
sub SUSAEK{


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

							if($kcodea =~ /A5/){
								$kqpoint += 1;
							}
				$rmax = int(320 - ($kchat*2));
				if($rmax < 220 ){
					$rmax = 220;
				}
				$r = int(rand($rmax));
				if($kcodea =~ /A7/ && $r < 30){
				$kqpoint += 1;
				&K_LOG("���� �� �ӿ��� �������� ��ฦ ã�ҽ��ϴ�!");
				}elsif( $r < 40 ){				
					$getgold = int(rand(50+$kchat))+50;
					$kgold += $getgold;
					&K_LOG("�����߿� �� <font color=red>$getgold</font>���� ã�Ƴ������ϴ�.");
				}elsif( $r < 46 ){
					if( int(rand(100+$kstrt)) > 100 ){
						$kstr += 1;
						&K_LOG("�����߿� ȣ���̰� ���ĿԽ��ϴ�!\n�׷��� $kname���� ȣ���̸� ���� �����ƽ��ϴ�.\n������ <font color=red>+1</font> ����Ͽ����ϴ�.");
					}else{
						&K_LOG("�����߿� ȣ���̰� ���ĿԽ��ϴ�!\n�׷��� $kname���� ���������ϴ�..");
					}
				}elsif( $r < 54 ){
					if( int(rand(100+$kstr)) > 100 ){
						$getgold = int(rand(50+$kchat))*2+200;
						$kgold += $getgold;
						&K_LOG("Ž���߿� ������ ���ĿԽ��ϴ�!\n�׷��� $kname�� ������ ����ϴµ� �����߽��ϴ�.\n�����ֹε��� ��$kname��, �츱 ����� ���� ������ ��ġ���ּż� �����մϴ�. ������ �޾��ֽʽÿ�!�� �� <font color=red>$getgold</font>�� �޾ҽ��ϴ�!");
					}else{
						&K_LOG("Ž���߿� ������ ���ĿԽ��ϴ�! $kname���� �й��ϰ� ���������ϴ�.");
					}
				}elsif( $r < 59 ){
					$getgold = int(rand(200-$kchat/2))+10;
					$kgold -= $getgold;
					if( $kgold < 0 ){
						$getgold = -$kgold;
						$kgold = 0;
					} 
					&K_LOG("�����߿� �� <font color=red>$getgold</font>�� ��������� ���ҽ��ϴ�!");
				}elsif( $r < 65 ){
					if( rand(25) < 1 ){
						$getpwr = +1;
						$kstr += $getpwr;
						$kint += $getpwr;
						$klea += $getpwr;
						$kcha += $getpwr;
						&K_LOG("Ž���߿� �� ������ �ٰ��Խ��ϴ�. ���� �������� �̸��� ����̶�� �մϴ�. �״�� ����ɷ��� ������ ������ ������ �ð��ຸ�ʽÿ�.�� ��� �ɷ�ġ�� <font color=red>$getpwr</font> ����Ͽ����ϴ�.");
					}
				}elsif( $r < 75 ){
					$rnd = int(rand($kchat+100));
					if( $rnd > 50 ){
						$kcha_ex += 5;
						&K_LOG("�����߿� ��� �ִ� ���ھָ� ã�Ƴ������ϴ�.\n�ƹ����� �θ� �Ҿ���� �� �����ϴ�.\n$kname���� 1�ð� �α��� ������ ���, �� ������ �θ� ã�Ƴ� ���� �־���.\n�ŷ°���ġ�� <font color=red>+5</font> ����Ͽ����ϴ�.");
					}else{
						&K_LOG("�����߿� ��� �ִ� ���ھָ� ã�Ƴ������ϴ�.\n�ƹ����� �θ� �Ҿ���� �� �����ϴ�.\n$kname���� 1�ð� �α��� ���������� ���������Ե� �� ������ �θ�� ã�Ƴ� ���� ������.\n����� ����������� �� ���̸� �ñ��� $kname���� �������ϴ�.");
					}
				}elsif( $r < 85 ){
					$kcha_ex += 3;
					&K_LOG("�����߿� ��ȸ�� ������ �޾ҽ��ϴ�.\n��$kname��, ���� ��ȸ�� �����Ⱑ �����ְ� �ִµ� $kname���� �������ֽÿ�.��\n����������κ��� ���� �����ް� ��ſ� �ð��� ���½��ϴ�.\n�ŷ°���ġ�� <font color=red>+3</font> ����Ͽ����ϴ�.");
				}elsif( $r < 100 ){
					$kint_ex += 3;
					&K_LOG("�����߿� �� ����� û�� �־����ϴ�.\n��$kname��, �츮�� ����Ͽ� ���ڸ� �������� �����ϴ�. ������ ��Ź�帳�ϴ�!�� \n$kname�� ������� ����� ���Ǹ� ������.\n�̿� ���ߵ��� ���� �⻵�Ͽ����ϴ�.\n���°���ġ�� <font color=red>+3</font> ����Ͽ����ϴ�.");
				}elsif( $r < 120 ){
					&K_LOG("Ȱ¦ ���� Ǫ���ϴ� �Ʒ� $kname�� ǳ���� ���� �Ѱ����� �ð��� ���´�. ��� �ɷ�ġ�� ����ġ�� <font color=red>+1</font> ����Ͽ����ϴ�.");
					$kstr_ex += 1;
					$kint_ex += 1;
					$klea_ex += 1;
					$kcha_ex += 1;
				}elsif( $r < 200 ){
					$kcha_ex += 1;

					@rmes = (
					"���� �̾߱�δ� �Ʒ��� ������ ���絵 �� ��������ϴ�.",
					"���� �̾߱�δ� ������ �뼺���� �ϰ� �Ǹ� ������ �跫���� �𸣰� �Ǵ� �� ��������.",
					"�ı��� ����ġ�� ������ �����ϱ� ����ϴٸ� �����ϰ� �Ǹ� ȿ���� ū �� �����ϴ�.",
					"Ž���߿� ������ ������ �ɷ�ġ�� �÷��ִ� �ϵ� �ִ� �� �����ϴ�.",
					"���� �����ϸ� ����� ����ǰ�� ������ ���� �ֽ��ϴ�.",
					"�ν��� �� ��Ƶθ� ���� �α��� �����ϱ� ����ϴ�.",
					"������ ������ �α��� �����ϱ� �����ϴ�.",
					"����� �����ϰ� ������ ����� �𿩵�ϴ�.",
					"����� ���� �ֵ� ���� ���÷κ��� ���� ��Ÿ���ϴ�.",
					"����ǰ�� 2���ۿ� ���� �� ���� ������ �����Ͻ�."
					);
					$r = int(rand(@rmes));
					&K_LOG("Ž���߿� ��������� �������ϴ�.\n�������:��$rmes[$r]��");
				}else{
				&K_LOG("�ƹ� �͵� �߰ߵ��� �ʾҽ��ϴ�.");
				}
				$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
					
}
1;

