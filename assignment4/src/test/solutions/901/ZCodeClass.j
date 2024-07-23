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

.method public static areDivisors(FF)Z
Label0:
.var 0 is num1 F from Label0 to Label1
.var 1 is num2 F from Label0 to Label1
.var 2 is for F from Label0 to Label1
	fload_0
	fload_1
	frem
	ldc 0.0000
	fcmpl
	ifeq Label2
	iconst_0
	goto Label3
Label2:
	iconst_1
Label3:
	fload_1
	fload_0
	frem
	ldc 0.0000
	fcmpl
	ifeq Label4
	iconst_0
	goto Label5
Label4:
	iconst_1
Label5:
	ior
	ireturn
Label1:
.limit stack 3
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is for F from Label0 to Label1
Label2:
.var 2 is num1 Ljava/lang/Object; from Label2 to Label3
	ldc 2.0000
	fstore_2
.var 3 is num2 Ljava/lang/Object; from Label2 to Label3
	ldc 4.0000
	fstore_3
	fload_2
	fload_3
	invokestatic ZCodeClass/areDivisors(FF)Z
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
.limit stack 2
.limit locals 4
.end method
