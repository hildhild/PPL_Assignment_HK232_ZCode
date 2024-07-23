.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object
.field static a [F

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
	ldc 2.0000
	f2i
	newarray float
	putstatic ZCodeClass.a [F
	return
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is for F from Label0 to Label1
Label2:
	getstatic ZCodeClass.a [F
	ldc 1.0000
	f2i
	getstatic ZCodeClass.a [F
	ldc 0.0000
	f2i
	faload
	ldc 1.0000
	fadd
	fastore
	getstatic ZCodeClass.a [F
	ldc 1.0000
	f2i
	faload
	invokestatic io/writeNumber(F)V
Label3:
	return
Label1:
.limit stack 5
.limit locals 2
.end method
