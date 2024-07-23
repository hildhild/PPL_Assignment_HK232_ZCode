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

.method public static foo(Ljava/lang/String;Z)V
Label0:
.var 0 is a Ljava/lang/String; from Label0 to Label1
.var 1 is b Z from Label0 to Label1
.var 2 is for F from Label0 to Label1
Label2:
	aload_0
	invokestatic io/writeString(Ljava/lang/String;)V
	iconst_1
	invokestatic io/writeBool(Z)V
Label3:
	return
Label1:
.limit stack 1
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is for F from Label0 to Label1
Label2:
	ldc "Votien"
	iconst_1
	invokestatic ZCodeClass/foo(Ljava/lang/String;Z)V
Label3:
	return
Label1:
.limit stack 2
.limit locals 2
.end method
