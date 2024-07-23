.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public <init>()V
Label0:
.var 0 is this LZCodeClass; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
	return
Label1:
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
	return
Label1:
.limit stack 0
.limit locals 0
.end method

.method public static isPrime(F)Z
Label0:
.var 0 is x F from Label0 to Label1
.var 1 is for F from Label0 to Label1
Label2:
	fload_0
	ldc 1.0000
	fcmpl
	ifgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label4
	iconst_0
	ireturn
Label4:
.var 2 is i Ljava/lang/Object; from Label2 to Label3
	ldc 2.0000
	fstore_2
	fload_2
	fstore_1
Label9:
	fload_2
	fload_0
	ldc 2.0000
	fdiv
	fcmpl
	ifle Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label8
Label12:
	fload_0
	fload_2
	frem
	ldc 0.0000
	fcmpl
	ifeq Label15
	iconst_0
	goto Label16
Label15:
	iconst_1
Label16:
	ifle Label14
	iconst_0
	ireturn
Label14:
Label13:
Label7:
	fload_2
	ldc 1.0000
	fadd
	fstore_2
	goto Label9
Label8:
	fload_1
	fstore_2
	iconst_1
	ireturn
Label3:
Label1:
.limit stack 4
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is for F from Label0 to Label1
Label2:
.var 2 is x F from Label2 to Label3
	ldc 24.0000
	fstore_2
	fload_2
	invokestatic ZCodeClass/isPrime(F)Z
	ifle Label5
	ldc "Yes"
	invokestatic io/writeString(Ljava/lang/String;)V
	goto Label4
Label5:
	ldc "No"
	invokestatic io/writeString(Ljava/lang/String;)V
Label4:
Label3:
	return
Label1:
.limit stack 1
.limit locals 3
.end method
