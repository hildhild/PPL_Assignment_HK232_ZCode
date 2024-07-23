.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object
.field static a [[[[F

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
	ldc 1.0000
	f2i
	anewarray [[[F
	dup
	ldc 0.0000
	f2i
	ldc 1.0000
	f2i
	anewarray [[F
	dup
	ldc 0.0000
	f2i
	ldc 1.0000
	f2i
	anewarray [F
	dup
	ldc 0.0000
	f2i
	ldc 1.0000
	f2i
	newarray float
	dup
	ldc 0.0000
	f2i
	ldc 1.0000
	fastore
	aastore
	aastore
	aastore
	putstatic ZCodeClass.a [[[[F
	return
Label1:
.limit stack 25
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is for F from Label0 to Label1
Label2:
.var 2 is b Ljava/lang/Object; from Label2 to Label3
	getstatic ZCodeClass.a [[[[F
	ldc 0.0000
	f2i
	aaload
	astore_2
.var 3 is c Ljava/lang/Object; from Label2 to Label3
	aload_2
	ldc 0.0000
	f2i
	aaload
	astore_3
.var 4 is d Ljava/lang/Object; from Label2 to Label3
	aload_3
	ldc 0.0000
	f2i
	aaload
	astore 4
	getstatic ZCodeClass.a [[[[F
	ldc 0.0000
	f2i
	aaload
	ldc 0.0000
	f2i
	aaload
	ldc 0.0000
	f2i
	aaload
	ldc 0.0000
	f2i
	ldc 4.0000
	fastore
	aload 4
	ldc 0.0000
	f2i
	faload
	invokestatic io/writeNumber(F)V
Label3:
	return
Label1:
.limit stack 7
.limit locals 5
.end method
