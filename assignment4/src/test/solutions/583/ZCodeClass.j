.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object
.field static b [Z

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
	newarray boolean
	dup
	ldc 0.0000
	f2i
	iconst_1
	bastore
	putstatic ZCodeClass.b [Z
	return
Label1:
.limit stack 5
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is for F from Label0 to Label1
Label2:
.var 2 is a [[Z from Label2 to Label3
	ldc 2.0000
	f2i
	anewarray [Z
	dup
	ldc 0.0000
	f2i
	ldc 1.0000
	f2i
	newarray boolean
	dup
	ldc 0.0000
	f2i
	iconst_1
	bastore
	aastore
	dup
	ldc 1.0000
	f2i
	ldc 1.0000
	f2i
	newarray boolean
	dup
	ldc 0.0000
	f2i
	iconst_0
	bastore
	aastore
	astore_2
	aload_2
	ldc 1.0000
	f2i
	aaload
	ldc 0.0000
	f2i
	baload
	invokestatic io/writeBool(Z)V
	aload_2
	ldc 0.0000
	f2i
	aaload
	ldc 0.0000
	f2i
	baload
	invokestatic io/writeBool(Z)V
	getstatic ZCodeClass.b [Z
	ldc 0.0000
	f2i
	baload
	invokestatic io/writeBool(Z)V
Label3:
	return
Label1:
.limit stack 10
.limit locals 3
.end method
