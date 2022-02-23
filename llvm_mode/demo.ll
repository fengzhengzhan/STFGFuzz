; ModuleID = 'demo.cc'
source_filename = "demo.cc"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

%"class.std::ios_base::Init" = type { i8 }
%struct._IO_FILE = type { i32, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, %struct._IO_marker*, %struct._IO_FILE*, i32, i32, i64, i16, i8, [1 x i8], i8*, i64, %struct._IO_codecvt*, %struct._IO_wide_data*, %struct._IO_FILE*, i8*, i64, i32, [20 x i8] }
%struct._IO_marker = type opaque
%struct._IO_codecvt = type opaque
%struct._IO_wide_data = type opaque

$"__cxx_global_var_init$21576b91ab9b15712202e1b4a494877f" = comdat any

$main = comdat any

$"_GLOBAL__sub_I_demo.cc$21576b91ab9b15712202e1b4a494877f" = comdat any

$sancov.module_ctor_trace_pc_guard = comdat any

@_ZStL8__ioinit = internal global { %"class.std::ios_base::Init", [63 x i8] } zeroinitializer, align 32
@__dso_handle = external hidden global i8
@.str = internal constant { [21 x i8], [43 x i8] } { [21 x i8] c"The quick brown fox \00", [43 x i8] zeroinitializer }, align 32
@.str.1 = internal constant { [12 x i8], [52 x i8] } { [12 x i8] c"jumps over \00", [52 x i8] zeroinitializer }, align 32
@.str.2 = internal constant { [13 x i8], [51 x i8] } { [13 x i8] c"the lazy dog\00", [51 x i8] zeroinitializer }, align 32
@stdin = external dso_local global %struct._IO_FILE*, align 8
@.str.3 = internal constant { [26 x i8], [38 x i8] } { [26 x i8] c"Puzzle solved, congrats!\0A\00", [38 x i8] zeroinitializer }, align 32
@__sancov_lowest_stack = external thread_local(initialexec) global i64
@__sancov_gen_ = private global [1 x i32] zeroinitializer, section "__sancov_guards", comdat($"__cxx_global_var_init$21576b91ab9b15712202e1b4a494877f"), align 4, !associated !0
@__sancov_gen_.4 = private global [8 x i32] zeroinitializer, section "__sancov_guards", comdat($main), align 4, !associated !1
@__sancov_gen_cov_switch_values = internal global [3 x i64] [i64 1, i64 32, i64 48879]
@__sancov_gen_.5 = private global [1 x i32] zeroinitializer, section "__sancov_guards", comdat($"_GLOBAL__sub_I_demo.cc$21576b91ab9b15712202e1b4a494877f"), align 4, !associated !2
@__start___sancov_guards = external hidden global i32
@__stop___sancov_guards = external hidden global i32
@__asan_option_detect_stack_use_after_return = external global i32
@___asan_gen_ = private unnamed_addr constant [47 x i8] c"4 32 44 6 buffer 112 8 1 x 144 4 1 y 160 2 1 z\00", align 1
@___asan_gen_.6 = private constant [8 x i8] c"demo.cc\00", align 1
@___asan_gen_.7 = private unnamed_addr constant [14 x i8] c"std::__ioinit\00", align 1
@___asan_gen_.8 = private unnamed_addr constant [67 x i8] c"/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/iostream\00", align 1
@___asan_gen_.9 = private unnamed_addr constant { [67 x i8]*, i32, i32 } { [67 x i8]* @___asan_gen_.8, i32 74, i32 25 }
@___asan_gen_.10 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.11 = private unnamed_addr constant [8 x i8] c"demo.cc\00", align 1
@___asan_gen_.12 = private unnamed_addr constant { [8 x i8]*, i32, i32 } { [8 x i8]* @___asan_gen_.11, i32 38, i32 26 }
@___asan_gen_.13 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.14 = private unnamed_addr constant [8 x i8] c"demo.cc\00", align 1
@___asan_gen_.15 = private unnamed_addr constant { [8 x i8]*, i32, i32 } { [8 x i8]* @___asan_gen_.14, i32 39, i32 28 }
@___asan_gen_.16 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.17 = private unnamed_addr constant [8 x i8] c"demo.cc\00", align 1
@___asan_gen_.18 = private unnamed_addr constant { [8 x i8]*, i32, i32 } { [8 x i8]* @___asan_gen_.17, i32 40, i32 27 }
@___asan_gen_.19 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.20 = private unnamed_addr constant [8 x i8] c"demo.cc\00", align 1
@___asan_gen_.21 = private unnamed_addr constant { [8 x i8]*, i32, i32 } { [8 x i8]* @___asan_gen_.20, i32 67, i32 10 }
@llvm.compiler.used = appending global [8 x i8*] [i8* bitcast ([1 x i32]* @__sancov_gen_ to i8*), i8* bitcast ([8 x i32]* @__sancov_gen_.4 to i8*), i8* bitcast ([1 x i32]* @__sancov_gen_.5 to i8*), i8* getelementptr inbounds ({ %"class.std::ios_base::Init", [63 x i8] }, { %"class.std::ios_base::Init", [63 x i8] }* @_ZStL8__ioinit, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [21 x i8], [43 x i8] }, { [21 x i8], [43 x i8] }* @.str, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [12 x i8], [52 x i8] }, { [12 x i8], [52 x i8] }* @.str.1, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [13 x i8], [51 x i8] }, { [13 x i8], [51 x i8] }* @.str.2, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [26 x i8], [38 x i8] }, { [26 x i8], [38 x i8] }* @.str.3, i32 0, i32 0, i32 0)], section "llvm.metadata"
@0 = internal global [5 x { i64, i64, i64, i64, i64, i64, i64, i64 }] [{ i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ %"class.std::ios_base::Init", [63 x i8] }* @_ZStL8__ioinit to i64), i64 1, i64 64, i64 ptrtoint ([14 x i8]* @___asan_gen_.7 to i64), i64 ptrtoint ([8 x i8]* @___asan_gen_.6 to i64), i64 1, i64 ptrtoint ({ [67 x i8]*, i32, i32 }* @___asan_gen_.9 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [21 x i8], [43 x i8] }* @.str to i64), i64 21, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.10 to i64), i64 ptrtoint ([8 x i8]* @___asan_gen_.6 to i64), i64 0, i64 ptrtoint ({ [8 x i8]*, i32, i32 }* @___asan_gen_.12 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [12 x i8], [52 x i8] }* @.str.1 to i64), i64 12, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.13 to i64), i64 ptrtoint ([8 x i8]* @___asan_gen_.6 to i64), i64 0, i64 ptrtoint ({ [8 x i8]*, i32, i32 }* @___asan_gen_.15 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [13 x i8], [51 x i8] }* @.str.2 to i64), i64 13, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.16 to i64), i64 ptrtoint ([8 x i8]* @___asan_gen_.6 to i64), i64 0, i64 ptrtoint ({ [8 x i8]*, i32, i32 }* @___asan_gen_.18 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [26 x i8], [38 x i8] }* @.str.3 to i64), i64 26, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.19 to i64), i64 ptrtoint ([8 x i8]* @___asan_gen_.6 to i64), i64 0, i64 ptrtoint ({ [8 x i8]*, i32, i32 }* @___asan_gen_.21 to i64), i64 -1 }]
@llvm.global_ctors = appending global [3 x { i32, void ()*, i8* }] [{ i32, void ()*, i8* } { i32 65535, void ()* @_GLOBAL__sub_I_demo.cc, i8* null }, { i32, void ()*, i8* } { i32 2, void ()* @sancov.module_ctor_trace_pc_guard, i8* bitcast (void ()* @sancov.module_ctor_trace_pc_guard to i8*) }, { i32, void ()*, i8* } { i32 1, void ()* @asan.module_ctor, i8* null }]
@llvm.global_dtors = appending global [1 x { i32, void ()*, i8* }] [{ i32, void ()*, i8* } { i32 1, void ()* @asan.module_dtor, i8* null }]

; Function Attrs: noinline sanitize_address uwtable
define internal void @__cxx_global_var_init() #0 section ".text.startup" comdat($"__cxx_global_var_init$21576b91ab9b15712202e1b4a494877f") {
entry:
  call void @__sanitizer_cov_trace_pc_guard(i32* getelementptr inbounds ([1 x i32], [1 x i32]* @__sancov_gen_, i32 0, i32 0)) #8
  call void @_ZNSt8ios_base4InitC1Ev(%"class.std::ios_base::Init"* nonnull dereferenceable(1) getelementptr inbounds ({ %"class.std::ios_base::Init", [63 x i8] }, { %"class.std::ios_base::Init", [63 x i8] }* @_ZStL8__ioinit, i32 0, i32 0))
  %0 = call i32 @__cxa_atexit(void (i8*)* bitcast (void (%"class.std::ios_base::Init"*)* @_ZNSt8ios_base4InitD1Ev to void (i8*)*), i8* getelementptr inbounds ({ %"class.std::ios_base::Init", [63 x i8] }, { %"class.std::ios_base::Init", [63 x i8] }* @_ZStL8__ioinit, i32 0, i32 0, i32 0), i8* @__dso_handle) #3
  ret void
}

declare dso_local void @_ZNSt8ios_base4InitC1Ev(%"class.std::ios_base::Init"* nonnull dereferenceable(1)) unnamed_addr #1

; Function Attrs: nounwind
declare dso_local void @_ZNSt8ios_base4InitD1Ev(%"class.std::ios_base::Init"* nonnull dereferenceable(1)) unnamed_addr #2

; Function Attrs: nounwind
declare dso_local i32 @__cxa_atexit(void (i8*)*, i8*, i8*) #3

; Function Attrs: noinline norecurse optnone sanitize_address uwtable mustprogress
define dso_local i32 @main(i32 %argc, i8** %argv) #4 comdat {
entry:
  %retval = alloca i32, align 4
  %argc.addr = alloca i32, align 4
  %argv.addr = alloca i8**, align 8
  %cleanup.dest.slot = alloca i32, align 4
  %asan_local_stack_base = alloca i64, align 8
  %0 = load i32, i32* @__asan_option_detect_stack_use_after_return, align 4
  %1 = icmp ne i32 %0, 0
  br i1 %1, label %2, label %4

2:                                                ; preds = %entry
  %3 = call i64 @__asan_stack_malloc_2(i64 192)
  br label %4

4:                                                ; preds = %entry, %2
  %5 = phi i64 [ 0, %entry ], [ %3, %2 ]
  %6 = icmp eq i64 %5, 0
  br i1 %6, label %7, label %9

7:                                                ; preds = %4
  %MyAlloca = alloca i8, i64 192, align 32
  %8 = ptrtoint i8* %MyAlloca to i64
  br label %9

9:                                                ; preds = %4, %7
  %10 = phi i64 [ %5, %4 ], [ %8, %7 ]
  store i64 %10, i64* %asan_local_stack_base, align 8
  %11 = add i64 %10, 32
  %12 = inttoptr i64 %11 to [44 x i8]*
  %13 = add i64 %10, 112
  %14 = inttoptr i64 %13 to i64*
  %15 = add i64 %10, 144
  %16 = inttoptr i64 %15 to i32*
  %17 = add i64 %10, 160
  %18 = inttoptr i64 %17 to i16*
  %19 = inttoptr i64 %10 to i64*
  store i64 1102416563, i64* %19, align 8
  %20 = add i64 %10, 8
  %21 = inttoptr i64 %20 to i64*
  store i64 ptrtoint ([47 x i8]* @___asan_gen_ to i64), i64* %21, align 8
  %22 = add i64 %10, 16
  %23 = inttoptr i64 %22 to i64*
  store i64 ptrtoint (i32 (i32, i8**)* @main to i64), i64* %23, align 8
  %24 = lshr i64 %10, 3
  %25 = add i64 %24, 2147450880
  %26 = add i64 %25, 0
  %27 = inttoptr i64 %26 to i64*
  store i64 -506381209984437775, i64* %27, align 1
  %28 = add i64 %25, 8
  %29 = inttoptr i64 %28 to i64*
  store i64 -938733397034731272, i64* %29, align 1
  %30 = add i64 %25, 16
  %31 = inttoptr i64 %30 to i64*
  store i64 -868082052598533390, i64* %31, align 1
  call void @__sanitizer_cov_trace_pc_guard(i32* getelementptr inbounds ([8 x i32], [8 x i32]* @__sancov_gen_.4, i32 0, i32 0)) #8
  store i32 0, i32* %retval, align 4
  store i32 %argc, i32* %argc.addr, align 4
  store i8** %argv, i8*** %argv.addr, align 8
  %32 = bitcast [44 x i8]* %12 to i8*
  %33 = add i64 %25, 4
  %34 = inttoptr i64 %33 to i32*
  store i32 0, i32* %34, align 1
  %35 = add i64 %25, 8
  %36 = inttoptr i64 %35 to i16*
  store i16 1024, i16* %36, align 1
  call void @llvm.lifetime.start.p0i8(i64 44, i8* %32) #3
  %37 = bitcast [44 x i8]* %12 to i8*
  %38 = call i8* @__asan_memset(i8* %37, i32 0, i64 44)
  %arraydecay = getelementptr inbounds [44 x i8], [44 x i8]* %12, i64 0, i64 0
  %39 = load i8**, i8*** %argv.addr, align 8
  %arrayidx = getelementptr inbounds i8*, i8** %39, i64 1
  %40 = ptrtoint i8** %arrayidx to i64
  %41 = lshr i64 %40, 3
  %42 = add i64 %41, 2147450880
  %43 = inttoptr i64 %42 to i8*
  %44 = load i8, i8* %43, align 1
  %45 = icmp ne i8 %44, 0
  br i1 %45, label %46, label %47

46:                                               ; preds = %9
  call void @__asan_report_load8(i64 %40) #8
  unreachable

47:                                               ; preds = %9
  %48 = load i8*, i8** %arrayidx, align 8
  %49 = call i8* @__asan_memcpy(i8* %arraydecay, i8* %48, i64 44)
  %arrayidx1 = getelementptr inbounds [44 x i8], [44 x i8]* %12, i64 0, i64 0
  %call = call i32 @memcmp(i8* %arrayidx1, i8* getelementptr inbounds ({ [21 x i8], [43 x i8] }, { [21 x i8], [43 x i8] }* @.str, i32 0, i32 0, i64 0), i64 20) #9
  call void @__sanitizer_cov_trace_const_cmp4(i32 0, i32 %call)
  %cmp = icmp ne i32 %call, 0
  br i1 %cmp, label %entry.if.then_crit_edge, label %lor.lhs.false

entry.if.then_crit_edge:                          ; preds = %47
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([8 x i32]* @__sancov_gen_.4 to i64), i64 4) to i32*)) #8
  br label %if.then

lor.lhs.false:                                    ; preds = %47
  %arrayidx2 = getelementptr inbounds [44 x i8], [44 x i8]* %12, i64 0, i64 20
  %call3 = call i32 @strncmp(i8* %arrayidx2, i8* getelementptr inbounds ({ [12 x i8], [52 x i8] }, { [12 x i8], [52 x i8] }* @.str.1, i32 0, i32 0, i64 0), i64 11) #10
  call void @__sanitizer_cov_trace_const_cmp4(i32 0, i32 %call3)
  %cmp4 = icmp ne i32 %call3, 0
  br i1 %cmp4, label %lor.lhs.false.if.then_crit_edge, label %lor.lhs.false5

lor.lhs.false.if.then_crit_edge:                  ; preds = %lor.lhs.false
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([8 x i32]* @__sancov_gen_.4 to i64), i64 8) to i32*)) #8
  br label %if.then

lor.lhs.false5:                                   ; preds = %lor.lhs.false
  %arrayidx6 = getelementptr inbounds [44 x i8], [44 x i8]* %12, i64 0, i64 31
  %call7 = call i32 @strcmp(i8* %arrayidx6, i8* getelementptr inbounds ({ [13 x i8], [51 x i8] }, { [13 x i8], [51 x i8] }* @.str.2, i32 0, i32 0, i64 0)) #9
  call void @__sanitizer_cov_trace_const_cmp4(i32 0, i32 %call7)
  %cmp8 = icmp ne i32 %call7, 0
  br i1 %cmp8, label %lor.lhs.false5.if.then_crit_edge, label %if.end

lor.lhs.false5.if.then_crit_edge:                 ; preds = %lor.lhs.false5
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([8 x i32]* @__sancov_gen_.4 to i64), i64 12) to i32*)) #8
  br label %if.then

if.then:                                          ; preds = %lor.lhs.false5.if.then_crit_edge, %lor.lhs.false.if.then_crit_edge, %entry.if.then_crit_edge
  store i32 1, i32* %retval, align 4
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup21

if.end:                                           ; preds = %lor.lhs.false5
  %50 = bitcast i64* %14 to i8*
  %51 = add i64 %25, 14
  %52 = inttoptr i64 %51 to i8*
  store i8 0, i8* %52, align 1
  call void @llvm.lifetime.start.p0i8(i64 8, i8* %50) #3
  %53 = ptrtoint i64* %14 to i64
  %54 = lshr i64 %53, 3
  %55 = add i64 %54, 2147450880
  %56 = inttoptr i64 %55 to i8*
  %57 = load i8, i8* %56, align 1
  %58 = icmp ne i8 %57, 0
  br i1 %58, label %59, label %60

59:                                               ; preds = %if.end
  call void @__asan_report_store8(i64 %53) #8
  unreachable

60:                                               ; preds = %if.end
  store i64 0, i64* %14, align 8
  %61 = bitcast i64* %14 to i8*
  %62 = load i8, i8* inttoptr (i64 add (i64 lshr (i64 ptrtoint (%struct._IO_FILE** @stdin to i64), i64 3), i64 2147450880) to i8*), align 1
  %63 = icmp ne i8 %62, 0
  br i1 %63, label %64, label %65

64:                                               ; preds = %60
  call void @__asan_report_load8(i64 ptrtoint (%struct._IO_FILE** @stdin to i64)) #8
  unreachable

65:                                               ; preds = %60
  %66 = load %struct._IO_FILE*, %struct._IO_FILE** @stdin, align 8
  %call9 = call i64 @fread(i8* %61, i64 8, i64 1, %struct._IO_FILE* %66)
  %67 = ptrtoint i64* %14 to i64
  %68 = lshr i64 %67, 3
  %69 = add i64 %68, 2147450880
  %70 = inttoptr i64 %69 to i8*
  %71 = load i8, i8* %70, align 1
  %72 = icmp ne i8 %71, 0
  br i1 %72, label %73, label %74

73:                                               ; preds = %65
  call void @__asan_report_load8(i64 %67) #8
  unreachable

74:                                               ; preds = %65
  %75 = load i64, i64* %14, align 8
  call void @__sanitizer_cov_trace_const_cmp8(i64 -3819410105351357762, i64 %75)
  %cmp10 = icmp ne i64 %75, -3819410105351357762
  br i1 %cmp10, label %if.then11, label %if.end12

if.then11:                                        ; preds = %74
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([8 x i32]* @__sancov_gen_.4 to i64), i64 16) to i32*)) #8
  store i32 1, i32* %retval, align 4
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup20

if.end12:                                         ; preds = %74
  %76 = bitcast i32* %16 to i8*
  %77 = add i64 %25, 18
  %78 = inttoptr i64 %77 to i8*
  store i8 4, i8* %78, align 1
  call void @llvm.lifetime.start.p0i8(i64 4, i8* %76) #3
  %79 = ptrtoint i32* %16 to i64
  %80 = lshr i64 %79, 3
  %81 = add i64 %80, 2147450880
  %82 = inttoptr i64 %81 to i8*
  %83 = load i8, i8* %82, align 1
  %84 = icmp ne i8 %83, 0
  br i1 %84, label %85, label %91, !prof !15

85:                                               ; preds = %if.end12
  %86 = and i64 %79, 7
  %87 = add i64 %86, 3
  %88 = trunc i64 %87 to i8
  %89 = icmp sge i8 %88, %83
  br i1 %89, label %90, label %91

90:                                               ; preds = %85
  call void @__asan_report_store4(i64 %79) #8
  unreachable

91:                                               ; preds = %85, %if.end12
  store i32 0, i32* %16, align 4
  %92 = bitcast i32* %16 to i8*
  %93 = load i8, i8* inttoptr (i64 add (i64 lshr (i64 ptrtoint (%struct._IO_FILE** @stdin to i64), i64 3), i64 2147450880) to i8*), align 1
  %94 = icmp ne i8 %93, 0
  br i1 %94, label %95, label %96

95:                                               ; preds = %91
  call void @__asan_report_load8(i64 ptrtoint (%struct._IO_FILE** @stdin to i64)) #8
  unreachable

96:                                               ; preds = %91
  %97 = load %struct._IO_FILE*, %struct._IO_FILE** @stdin, align 8
  %call13 = call i64 @fread(i8* %92, i64 4, i64 1, %struct._IO_FILE* %97)
  %98 = ptrtoint i32* %16 to i64
  %99 = lshr i64 %98, 3
  %100 = add i64 %99, 2147450880
  %101 = inttoptr i64 %100 to i8*
  %102 = load i8, i8* %101, align 1
  %103 = icmp ne i8 %102, 0
  br i1 %103, label %104, label %110, !prof !15

104:                                              ; preds = %96
  %105 = and i64 %98, 7
  %106 = add i64 %105, 3
  %107 = trunc i64 %106 to i8
  %108 = icmp sge i8 %107, %102
  br i1 %108, label %109, label %110

109:                                              ; preds = %104
  call void @__asan_report_load4(i64 %98) #8
  unreachable

110:                                              ; preds = %104, %96
  %111 = load i32, i32* %16, align 4
  call void @__sanitizer_cov_trace_const_cmp4(i32 -559038242, i32 %111)
  %cmp14 = icmp ne i32 %111, -559038242
  br i1 %cmp14, label %if.then15, label %if.end16

if.then15:                                        ; preds = %110
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([8 x i32]* @__sancov_gen_.4 to i64), i64 20) to i32*)) #8
  store i32 1, i32* %retval, align 4
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup19

if.end16:                                         ; preds = %110
  %112 = bitcast i16* %18 to i8*
  %113 = add i64 %25, 20
  %114 = inttoptr i64 %113 to i8*
  store i8 2, i8* %114, align 1
  call void @llvm.lifetime.start.p0i8(i64 2, i8* %112) #3
  %115 = ptrtoint i16* %18 to i64
  %116 = lshr i64 %115, 3
  %117 = add i64 %116, 2147450880
  %118 = inttoptr i64 %117 to i8*
  %119 = load i8, i8* %118, align 1
  %120 = icmp ne i8 %119, 0
  br i1 %120, label %121, label %127, !prof !15

121:                                              ; preds = %if.end16
  %122 = and i64 %115, 7
  %123 = add i64 %122, 1
  %124 = trunc i64 %123 to i8
  %125 = icmp sge i8 %124, %119
  br i1 %125, label %126, label %127

126:                                              ; preds = %121
  call void @__asan_report_store2(i64 %115) #8
  unreachable

127:                                              ; preds = %121, %if.end16
  store i16 0, i16* %18, align 2
  %128 = bitcast i16* %18 to i8*
  %129 = load i8, i8* inttoptr (i64 add (i64 lshr (i64 ptrtoint (%struct._IO_FILE** @stdin to i64), i64 3), i64 2147450880) to i8*), align 1
  %130 = icmp ne i8 %129, 0
  br i1 %130, label %131, label %132

131:                                              ; preds = %127
  call void @__asan_report_load8(i64 ptrtoint (%struct._IO_FILE** @stdin to i64)) #8
  unreachable

132:                                              ; preds = %127
  %133 = load %struct._IO_FILE*, %struct._IO_FILE** @stdin, align 8
  %call17 = call i64 @fread(i8* %128, i64 2, i64 1, %struct._IO_FILE* %133)
  %134 = ptrtoint i16* %18 to i64
  %135 = lshr i64 %134, 3
  %136 = add i64 %135, 2147450880
  %137 = inttoptr i64 %136 to i8*
  %138 = load i8, i8* %137, align 1
  %139 = icmp ne i8 %138, 0
  br i1 %139, label %140, label %146, !prof !15

140:                                              ; preds = %132
  %141 = and i64 %134, 7
  %142 = add i64 %141, 1
  %143 = trunc i64 %142 to i8
  %144 = icmp sge i8 %143, %138
  br i1 %144, label %145, label %146

145:                                              ; preds = %140
  call void @__asan_report_load2(i64 %134) #8
  unreachable

146:                                              ; preds = %140, %132
  %147 = load i16, i16* %18, align 2
  %conv = zext i16 %147 to i32
  %148 = zext i32 %conv to i64
  call void @__sanitizer_cov_trace_switch(i64 %148, i64* getelementptr inbounds ([3 x i64], [3 x i64]* @__sancov_gen_cov_switch_values, i32 0, i32 0))
  switch i32 %conv, label %sw.default [
    i32 48879, label %sw.bb
  ]

sw.bb:                                            ; preds = %146
  br label %sw.epilog

sw.default:                                       ; preds = %146
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([8 x i32]* @__sancov_gen_.4 to i64), i64 24) to i32*)) #8
  store i32 1, i32* %retval, align 4
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup

sw.epilog:                                        ; preds = %sw.bb
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([8 x i32]* @__sancov_gen_.4 to i64), i64 28) to i32*)) #8
  %call18 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ({ [26 x i8], [38 x i8] }, { [26 x i8], [38 x i8] }* @.str.3, i32 0, i32 0, i64 0))
  store i32 0, i32* %retval, align 4
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup

cleanup:                                          ; preds = %sw.epilog, %sw.default
  %149 = bitcast i16* %18 to i8*
  %150 = add i64 %25, 20
  %151 = inttoptr i64 %150 to i8*
  store i8 -8, i8* %151, align 1
  call void @llvm.lifetime.end.p0i8(i64 2, i8* %149) #3
  br label %cleanup19

cleanup19:                                        ; preds = %cleanup, %if.then15
  %152 = bitcast i32* %16 to i8*
  %153 = add i64 %25, 18
  %154 = inttoptr i64 %153 to i8*
  store i8 -8, i8* %154, align 1
  call void @llvm.lifetime.end.p0i8(i64 4, i8* %152) #3
  br label %cleanup20

cleanup20:                                        ; preds = %cleanup19, %if.then11
  %155 = bitcast i64* %14 to i8*
  %156 = add i64 %25, 14
  %157 = inttoptr i64 %156 to i8*
  store i8 -8, i8* %157, align 1
  call void @llvm.lifetime.end.p0i8(i64 8, i8* %155) #3
  br label %cleanup21

cleanup21:                                        ; preds = %cleanup20, %if.then
  %158 = bitcast [44 x i8]* %12 to i8*
  %159 = add i64 %25, 4
  %160 = inttoptr i64 %159 to i32*
  store i32 -117901064, i32* %160, align 1
  %161 = add i64 %25, 8
  %162 = inttoptr i64 %161 to i16*
  store i16 -1800, i16* %162, align 1
  call void @llvm.lifetime.end.p0i8(i64 44, i8* %158) #3
  %163 = load i32, i32* %retval, align 4
  store i64 1172321806, i64* %19, align 8
  %164 = icmp ne i64 %5, 0
  br i1 %164, label %165, label %178

165:                                              ; preds = %cleanup21
  %166 = add i64 %25, 0
  %167 = inttoptr i64 %166 to i64*
  store i64 -723401728380766731, i64* %167, align 1
  %168 = add i64 %25, 8
  %169 = inttoptr i64 %168 to i64*
  store i64 -723401728380766731, i64* %169, align 1
  %170 = add i64 %25, 16
  %171 = inttoptr i64 %170 to i64*
  store i64 -723401728380766731, i64* %171, align 1
  %172 = add i64 %25, 24
  %173 = inttoptr i64 %172 to i64*
  store i64 -723401728380766731, i64* %173, align 1
  %174 = add i64 %5, 248
  %175 = inttoptr i64 %174 to i64*
  %176 = load i64, i64* %175, align 8
  %177 = inttoptr i64 %176 to i8*
  store i8 0, i8* %177, align 1
  br label %185

178:                                              ; preds = %cleanup21
  %179 = add i64 %25, 0
  %180 = inttoptr i64 %179 to i64*
  store i64 0, i64* %180, align 1
  %181 = add i64 %25, 8
  %182 = inttoptr i64 %181 to i64*
  store i64 0, i64* %182, align 1
  %183 = add i64 %25, 16
  %184 = inttoptr i64 %183 to i64*
  store i64 0, i64* %184, align 1
  br label %185

185:                                              ; preds = %178, %165
  ret i32 %163
}

; Function Attrs: argmemonly nofree nosync nounwind willreturn
declare void @llvm.lifetime.start.p0i8(i64 immarg, i8* nocapture) #5

; Function Attrs: argmemonly nofree nosync nounwind willreturn writeonly
declare void @llvm.memset.p0i8.i64(i8* nocapture writeonly, i8, i64, i1 immarg) #6

; Function Attrs: argmemonly nofree nosync nounwind willreturn
declare void @llvm.memcpy.p0i8.p0i8.i64(i8* noalias nocapture writeonly, i8* noalias nocapture readonly, i64, i1 immarg) #5

; Function Attrs: nounwind readonly willreturn
declare dso_local i32 @memcmp(i8*, i8*, i64) #7

; Function Attrs: nounwind readonly willreturn
declare dso_local i32 @strncmp(i8*, i8*, i64) #7

; Function Attrs: nounwind readonly willreturn
declare dso_local i32 @strcmp(i8*, i8*) #7

declare dso_local i64 @fread(i8*, i64, i64, %struct._IO_FILE*) #1

declare dso_local i32 @printf(i8*, ...) #1

; Function Attrs: argmemonly nofree nosync nounwind willreturn
declare void @llvm.lifetime.end.p0i8(i64 immarg, i8* nocapture) #5

; Function Attrs: noinline sanitize_address uwtable
define internal void @_GLOBAL__sub_I_demo.cc() #0 section ".text.startup" comdat($"_GLOBAL__sub_I_demo.cc$21576b91ab9b15712202e1b4a494877f") {
entry:
  call void @__asan_before_dynamic_init(i64 ptrtoint ([8 x i8]* @___asan_gen_.6 to i64))
  call void @__sanitizer_cov_trace_pc_guard(i32* getelementptr inbounds ([1 x i32], [1 x i32]* @__sancov_gen_.5, i32 0, i32 0)) #8
  call void @__cxx_global_var_init()
  call void @__asan_after_dynamic_init()
  ret void
}

declare void @__sanitizer_cov_trace_pc_indir(i64)

declare void @__sanitizer_cov_trace_cmp1(i8 zeroext, i8 zeroext)

declare void @__sanitizer_cov_trace_cmp2(i16 zeroext, i16 zeroext)

declare void @__sanitizer_cov_trace_cmp4(i32 zeroext, i32 zeroext)

declare void @__sanitizer_cov_trace_cmp8(i64, i64)

declare void @__sanitizer_cov_trace_const_cmp1(i8 zeroext, i8 zeroext)

declare void @__sanitizer_cov_trace_const_cmp2(i16 zeroext, i16 zeroext)

declare void @__sanitizer_cov_trace_const_cmp4(i32 zeroext, i32 zeroext)

declare void @__sanitizer_cov_trace_const_cmp8(i64, i64)

declare void @__sanitizer_cov_trace_div4(i32 zeroext)

declare void @__sanitizer_cov_trace_div8(i64)

declare void @__sanitizer_cov_trace_gep(i64)

declare void @__sanitizer_cov_trace_switch(i64, i64*)

declare void @__sanitizer_cov_trace_pc()

declare void @__sanitizer_cov_trace_pc_guard(i32*)

declare void @__sanitizer_cov_trace_pc_guard_init(i32*, i32*)

define internal void @sancov.module_ctor_trace_pc_guard() comdat {
  call void @__asan_before_dynamic_init(i64 ptrtoint ([8 x i8]* @___asan_gen_.6 to i64))
  call void @__sanitizer_cov_trace_pc_guard_init(i32* @__start___sancov_guards, i32* @__stop___sancov_guards)
  call void @__asan_after_dynamic_init()
  ret void
}

declare void @__asan_report_load_n(i64, i64)

declare void @__asan_loadN(i64, i64)

declare void @__asan_report_load1(i64)

declare void @__asan_load1(i64)

declare void @__asan_report_load2(i64)

declare void @__asan_load2(i64)

declare void @__asan_report_load4(i64)

declare void @__asan_load4(i64)

declare void @__asan_report_load8(i64)

declare void @__asan_load8(i64)

declare void @__asan_report_load16(i64)

declare void @__asan_load16(i64)

declare void @__asan_report_store_n(i64, i64)

declare void @__asan_storeN(i64, i64)

declare void @__asan_report_store1(i64)

declare void @__asan_store1(i64)

declare void @__asan_report_store2(i64)

declare void @__asan_store2(i64)

declare void @__asan_report_store4(i64)

declare void @__asan_store4(i64)

declare void @__asan_report_store8(i64)

declare void @__asan_store8(i64)

declare void @__asan_report_store16(i64)

declare void @__asan_store16(i64)

declare void @__asan_report_exp_load_n(i64, i64, i32)

declare void @__asan_exp_loadN(i64, i64, i32)

declare void @__asan_report_exp_load1(i64, i32)

declare void @__asan_exp_load1(i64, i32)

declare void @__asan_report_exp_load2(i64, i32)

declare void @__asan_exp_load2(i64, i32)

declare void @__asan_report_exp_load4(i64, i32)

declare void @__asan_exp_load4(i64, i32)

declare void @__asan_report_exp_load8(i64, i32)

declare void @__asan_exp_load8(i64, i32)

declare void @__asan_report_exp_load16(i64, i32)

declare void @__asan_exp_load16(i64, i32)

declare void @__asan_report_exp_store_n(i64, i64, i32)

declare void @__asan_exp_storeN(i64, i64, i32)

declare void @__asan_report_exp_store1(i64, i32)

declare void @__asan_exp_store1(i64, i32)

declare void @__asan_report_exp_store2(i64, i32)

declare void @__asan_exp_store2(i64, i32)

declare void @__asan_report_exp_store4(i64, i32)

declare void @__asan_exp_store4(i64, i32)

declare void @__asan_report_exp_store8(i64, i32)

declare void @__asan_exp_store8(i64, i32)

declare void @__asan_report_exp_store16(i64, i32)

declare void @__asan_exp_store16(i64, i32)

declare i8* @__asan_memmove(i8*, i8*, i64)

declare i8* @__asan_memcpy(i8*, i8*, i64)

declare i8* @__asan_memset(i8*, i32, i64)

declare void @__asan_handle_no_return()

declare void @__sanitizer_ptr_cmp(i64, i64)

declare void @__sanitizer_ptr_sub(i64, i64)

declare i64 @__asan_stack_malloc_0(i64)

declare void @__asan_stack_free_0(i64, i64)

declare i64 @__asan_stack_malloc_1(i64)

declare void @__asan_stack_free_1(i64, i64)

declare i64 @__asan_stack_malloc_2(i64)

declare void @__asan_stack_free_2(i64, i64)

declare i64 @__asan_stack_malloc_3(i64)

declare void @__asan_stack_free_3(i64, i64)

declare i64 @__asan_stack_malloc_4(i64)

declare void @__asan_stack_free_4(i64, i64)

declare i64 @__asan_stack_malloc_5(i64)

declare void @__asan_stack_free_5(i64, i64)

declare i64 @__asan_stack_malloc_6(i64)

declare void @__asan_stack_free_6(i64, i64)

declare i64 @__asan_stack_malloc_7(i64)

declare void @__asan_stack_free_7(i64, i64)

declare i64 @__asan_stack_malloc_8(i64)

declare void @__asan_stack_free_8(i64, i64)

declare i64 @__asan_stack_malloc_9(i64)

declare void @__asan_stack_free_9(i64, i64)

declare i64 @__asan_stack_malloc_10(i64)

declare void @__asan_stack_free_10(i64, i64)

declare void @__asan_poison_stack_memory(i64, i64)

declare void @__asan_unpoison_stack_memory(i64, i64)

declare void @__asan_set_shadow_00(i64, i64)

declare void @__asan_set_shadow_f1(i64, i64)

declare void @__asan_set_shadow_f2(i64, i64)

declare void @__asan_set_shadow_f3(i64, i64)

declare void @__asan_set_shadow_f5(i64, i64)

declare void @__asan_set_shadow_f8(i64, i64)

declare void @__asan_alloca_poison(i64, i64)

declare void @__asan_allocas_unpoison(i64, i64)

declare void @__asan_before_dynamic_init(i64)

declare void @__asan_after_dynamic_init()

declare void @__asan_register_globals(i64, i64)

declare void @__asan_unregister_globals(i64, i64)

declare void @__asan_register_image_globals(i64)

declare void @__asan_unregister_image_globals(i64)

declare void @__asan_register_elf_globals(i64, i64, i64)

declare void @__asan_unregister_elf_globals(i64, i64, i64)

declare void @__asan_init()

define internal void @asan.module_ctor() {
  call void @__asan_init()
  call void @__asan_version_mismatch_check_v8()
  call void @__asan_register_globals(i64 ptrtoint ([5 x { i64, i64, i64, i64, i64, i64, i64, i64 }]* @0 to i64), i64 5)
  ret void
}

declare void @__asan_version_mismatch_check_v8()

define internal void @asan.module_dtor() {
  call void @__asan_unregister_globals(i64 ptrtoint ([5 x { i64, i64, i64, i64, i64, i64, i64, i64 }]* @0 to i64), i64 5)
  ret void
}

attributes #0 = { noinline sanitize_address uwtable "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { nounwind "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { nounwind }
attributes #4 = { noinline norecurse optnone sanitize_address uwtable mustprogress "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #5 = { argmemonly nofree nosync nounwind willreturn }
attributes #6 = { argmemonly nofree nosync nounwind willreturn writeonly }
attributes #7 = { nounwind readonly willreturn "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #8 = { nomerge }
attributes #9 = { nobuiltin nounwind readonly willreturn }
attributes #10 = { nounwind readonly willreturn }

!llvm.asan.globals = !{!3, !5, !7, !9, !11}
!llvm.module.flags = !{!13}
!llvm.ident = !{!14}

!0 = !{void ()* @__cxx_global_var_init}
!1 = !{i32 (i32, i8**)* @main}
!2 = !{void ()* @_GLOBAL__sub_I_demo.cc}
!3 = !{%"class.std::ios_base::Init"* getelementptr inbounds ({ %"class.std::ios_base::Init", [63 x i8] }, { %"class.std::ios_base::Init", [63 x i8] }* @_ZStL8__ioinit, i32 0, i32 0), !4, !"std::__ioinit", i1 true, i1 false}
!4 = !{!"/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/iostream", i32 74, i32 25}
!5 = !{[21 x i8]* getelementptr inbounds ({ [21 x i8], [43 x i8] }, { [21 x i8], [43 x i8] }* @.str, i32 0, i32 0), !6, !"<string literal>", i1 false, i1 false}
!6 = !{!"demo.cc", i32 38, i32 26}
!7 = !{[12 x i8]* getelementptr inbounds ({ [12 x i8], [52 x i8] }, { [12 x i8], [52 x i8] }* @.str.1, i32 0, i32 0), !8, !"<string literal>", i1 false, i1 false}
!8 = !{!"demo.cc", i32 39, i32 28}
!9 = !{[13 x i8]* getelementptr inbounds ({ [13 x i8], [51 x i8] }, { [13 x i8], [51 x i8] }* @.str.2, i32 0, i32 0), !10, !"<string literal>", i1 false, i1 false}
!10 = !{!"demo.cc", i32 40, i32 27}
!11 = !{[26 x i8]* getelementptr inbounds ({ [26 x i8], [38 x i8] }, { [26 x i8], [38 x i8] }* @.str.3, i32 0, i32 0), !12, !"<string literal>", i1 false, i1 false}
!12 = !{!"demo.cc", i32 67, i32 10}
!13 = !{i32 1, !"wchar_size", i32 4}
!14 = !{!"clang version 12.0.1 (git@github.com:fengzhengzhan/BTFuzz.git 0b64f5806b4302732328fa068687800669443ef8)"}
!15 = !{!"branch_weights", i32 1, i32 100000}
