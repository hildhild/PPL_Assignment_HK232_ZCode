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
.var 2 is a [[F from Label2 to Label3
	ldc 2.0000
	f2i
	ldc 2.0000
	f2i
	multianewarray [[F 2
	astore_2
	aload_2
	ldc 1.0000
	f2i
	aaload
	ldc 1.0000
	f2i
	aload_2
	ldc 0.0000
	f2i
	aaload
	ldc 0.0000
	f2i
	faload
	ldc 1.0000
	fadd
	fastore
	aload_2
	ldc 1.0000
	f2i
	aaload
	ldc 1.0000
	f2i
	faload
	invokestatic io/writeNumber(F)V
Label3:
	return
Label1:
.limit stack 6
.limit locals 3
.end method
