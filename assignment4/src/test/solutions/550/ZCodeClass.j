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

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is for F from Label0 to Label1
Label2:
	ldc 2.0000
	ldc 3.0000
	fcmpl
	ifle Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label7
	ldc 1.0000
	invokestatic io/writeNumber(F)V
	goto Label4
Label7:
	ldc 0.0000
	invokestatic io/writeNumber(F)V
Label4:
Label3:
	return
Label1:
.limit stack 2
.limit locals 2
.end method
