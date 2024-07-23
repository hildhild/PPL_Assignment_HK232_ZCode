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

.method public static printArray([F)V
Label0:
.var 0 is x [F from Label0 to Label1
.var 1 is for F from Label0 to Label1
Label2:
.var 2 is i Ljava/lang/Object; from Label2 to Label3
	ldc 0.0000
	fstore_2
	fload_2
	fstore_1
Label6:
	fload_2
	ldc 10.0000
	fcmpl
	iflt Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label5
Label9:
	aload_0
	fload_2
	f2i
	aload_0
	fload_2
	f2i
	faload
	ldc 1.0000
	fadd
	fastore
Label10:
Label4:
	fload_2
	ldc 1.0000
	fadd
	fstore_2
	goto Label6
Label5:
	fload_1
	fstore_2
Label3:
	return
Label1:
.limit stack 6
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is for F from Label0 to Label1
Label2:
.var 2 is a Ljava/lang/Object; from Label2 to Label3
	ldc 10.0000
	f2i
	newarray float
	dup
	ldc 0.0000
	f2i
	ldc 1.0000
	fastore
	dup
	ldc 1.0000
	f2i
	ldc 2.0000
	fastore
	dup
	ldc 2.0000
	f2i
	ldc 3.0000
	fastore
	dup
	ldc 3.0000
	f2i
	ldc 4.0000
	fastore
	dup
	ldc 4.0000
	f2i
	ldc 5.0000
	fastore
	dup
	ldc 5.0000
	f2i
	ldc 6.0000
	fastore
	dup
	ldc 6.0000
	f2i
	ldc 7.0000
	fastore
	dup
	ldc 7.0000
	f2i
	ldc 8.0000
	fastore
	dup
	ldc 8.0000
	f2i
	ldc 9.0000
	fastore
	dup
	ldc 9.0000
	f2i
	ldc 10.0000
	fastore
	astore_2
	aload_2
	invokestatic ZCodeClass/printArray([F)V
.var 3 is i Ljava/lang/Object; from Label2 to Label3
	ldc 0.0000
	fstore_3
	fload_3
	fstore_1
Label6:
	fload_3
	ldc 10.0000
	fcmpl
	iflt Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label5
Label9:
	aload_2
	fload_3
	f2i
	faload
	invokestatic io/writeNumber(F)V
Label10:
Label4:
	fload_3
	ldc 1.0000
	fadd
	fstore_3
	goto Label6
Label5:
	fload_1
	fstore_3
Label3:
	return
Label1:
.limit stack 5
.limit locals 4
.end method
