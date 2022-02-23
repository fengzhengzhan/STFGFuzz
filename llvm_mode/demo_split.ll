; ModuleID = 'IR/demo.ll'
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
  br label %0

0:                                                ; preds = %entry
  %1 = call i32 @__cxa_atexit(void (i8*)* bitcast (void (%"class.std::ios_base::Init"*)* @_ZNSt8ios_base4InitD1Ev to void (i8*)*), i8* getelementptr inbounds ({ %"class.std::ios_base::Init", [63 x i8] }, { %"class.std::ios_base::Init", [63 x i8] }* @_ZStL8__ioinit, i32 0, i32 0, i32 0), i8* @__dso_handle) #3
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
  br label %0

0:                                                ; preds = %entry
  %asan_local_stack_base = alloca i64, align 8
  %1 = load i32, i32* @__asan_option_detect_stack_use_after_return, align 4
  %2 = icmp ne i32 %1, 0
  br i1 %2, label %3, label %6

3:                                                ; preds = %0
  %4 = call i64 @__asan_stack_malloc_2(i64 192)
  br label %5

5:                                                ; preds = %3
  br label %6

6:                                                ; preds = %5, %0
  %7 = phi i64 [ 0, %0 ], [ %4, %5 ]
  %8 = icmp eq i64 %7, 0
  br i1 %8, label %9, label %12

9:                                                ; preds = %6
  %MyAlloca = alloca i8, i64 192, align 32
  %10 = ptrtoint i8* %MyAlloca to i64
  br label %11

11:                                               ; preds = %9
  br label %12

12:                                               ; preds = %11, %6
  %13 = phi i64 [ %7, %6 ], [ %10, %11 ]
  store i64 %13, i64* %asan_local_stack_base, align 8
  %14 = add i64 %13, 32
  %15 = inttoptr i64 %14 to [44 x i8]*
  %16 = add i64 %13, 112
  %17 = inttoptr i64 %16 to i64*
  %18 = add i64 %13, 144
  %19 = inttoptr i64 %18 to i32*
  %20 = add i64 %13, 160
  %21 = inttoptr i64 %20 to i16*
  %22 = inttoptr i64 %13 to i64*
  store i64 1102416563, i64* %22, align 8
  %23 = add i64 %13, 8
  %24 = inttoptr i64 %23 to i64*
  store i64 ptrtoint ([47 x i8]* @___asan_gen_ to i64), i64* %24, align 8
  %25 = add i64 %13, 16
  %26 = inttoptr i64 %25 to i64*
  store i64 ptrtoint (i32 (i32, i8**)* @main to i64), i64* %26, align 8
  %27 = lshr i64 %13, 3
  %28 = add i64 %27, 2147450880
  %29 = add i64 %28, 0
  %30 = inttoptr i64 %29 to i64*
  store i64 -506381209984437775, i64* %30, align 1
  %31 = add i64 %28, 8
  %32 = inttoptr i64 %31 to i64*
  store i64 -938733397034731272, i64* %32, align 1
  %33 = add i64 %28, 16
  %34 = inttoptr i64 %33 to i64*
  store i64 -868082052598533390, i64* %34, align 1
  call void @__sanitizer_cov_trace_pc_guard(i32* getelementptr inbounds ([8 x i32], [8 x i32]* @__sancov_gen_.4, i32 0, i32 0)) #8
  store i32 0, i32* %retval, align 4
  store i32 %argc, i32* %argc.addr, align 4
  store i8** %argv, i8*** %argv.addr, align 8
  %35 = bitcast [44 x i8]* %15 to i8*
  %36 = add i64 %28, 4
  %37 = inttoptr i64 %36 to i32*
  store i32 0, i32* %37, align 1
  %38 = add i64 %28, 8
  %39 = inttoptr i64 %38 to i16*
  store i16 1024, i16* %39, align 1
  call void @llvm.lifetime.start.p0i8(i64 44, i8* %35) #3
  %40 = bitcast [44 x i8]* %15 to i8*
  %41 = call i8* @__asan_memset(i8* %40, i32 0, i64 44)
  %arraydecay = getelementptr inbounds [44 x i8], [44 x i8]* %15, i64 0, i64 0
  %42 = load i8**, i8*** %argv.addr, align 8
  %arrayidx = getelementptr inbounds i8*, i8** %42, i64 1
  %43 = ptrtoint i8** %arrayidx to i64
  %44 = lshr i64 %43, 3
  %45 = add i64 %44, 2147450880
  %46 = inttoptr i64 %45 to i8*
  %47 = load i8, i8* %46, align 1
  %48 = icmp ne i8 %47, 0
  br i1 %48, label %49, label %51

49:                                               ; preds = %12
  call void @__asan_report_load8(i64 %43) #8
  br label %50

50:                                               ; preds = %49
  unreachable

51:                                               ; preds = %12
  %52 = load i8*, i8** %arrayidx, align 8
  %53 = call i8* @__asan_memcpy(i8* %arraydecay, i8* %52, i64 44)
  %arrayidx1 = getelementptr inbounds [44 x i8], [44 x i8]* %15, i64 0, i64 0
  %call = call i32 @memcmp(i8* %arrayidx1, i8* getelementptr inbounds ({ [21 x i8], [43 x i8] }, { [21 x i8], [43 x i8] }* @.str, i32 0, i32 0, i64 0), i64 20) #9
  br label %54

54:                                               ; preds = %51
  call void @__sanitizer_cov_trace_const_cmp4(i32 0, i32 %call)
  %cmp = icmp ne i32 %call, 0
  br i1 %cmp, label %entry.if.then_crit_edge, label %lor.lhs.false

entry.if.then_crit_edge:                          ; preds = %54
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([8 x i32]* @__sancov_gen_.4 to i64), i64 4) to i32*)) #8
  br label %55

55:                                               ; preds = %entry.if.then_crit_edge
  br label %if.then

lor.lhs.false:                                    ; preds = %54
  %arrayidx2 = getelementptr inbounds [44 x i8], [44 x i8]* %15, i64 0, i64 20
  %call3 = call i32 @strncmp(i8* %arrayidx2, i8* getelementptr inbounds ({ [12 x i8], [52 x i8] }, { [12 x i8], [52 x i8] }* @.str.1, i32 0, i32 0, i64 0), i64 11) #10
  call void @__sanitizer_cov_trace_const_cmp4(i32 0, i32 %call3)
  br label %56

56:                                               ; preds = %lor.lhs.false
  %cmp4 = icmp ne i32 %call3, 0
  br i1 %cmp4, label %lor.lhs.false.if.then_crit_edge, label %lor.lhs.false5

lor.lhs.false.if.then_crit_edge:                  ; preds = %56
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([8 x i32]* @__sancov_gen_.4 to i64), i64 8) to i32*)) #8
  br label %57

57:                                               ; preds = %lor.lhs.false.if.then_crit_edge
  br label %if.then

lor.lhs.false5:                                   ; preds = %56
  %arrayidx6 = getelementptr inbounds [44 x i8], [44 x i8]* %15, i64 0, i64 31
  %call7 = call i32 @strcmp(i8* %arrayidx6, i8* getelementptr inbounds ({ [13 x i8], [51 x i8] }, { [13 x i8], [51 x i8] }* @.str.2, i32 0, i32 0, i64 0)) #9
  call void @__sanitizer_cov_trace_const_cmp4(i32 0, i32 %call7)
  br label %58

58:                                               ; preds = %lor.lhs.false5
  %cmp8 = icmp ne i32 %call7, 0
  br i1 %cmp8, label %lor.lhs.false5.if.then_crit_edge, label %if.end

lor.lhs.false5.if.then_crit_edge:                 ; preds = %58
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([8 x i32]* @__sancov_gen_.4 to i64), i64 12) to i32*)) #8
  br label %59

59:                                               ; preds = %lor.lhs.false5.if.then_crit_edge
  br label %if.then

if.then:                                          ; preds = %59, %57, %55
  store i32 1, i32* %retval, align 4
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %60

60:                                               ; preds = %if.then
  br label %cleanup21

if.end:                                           ; preds = %58
  %61 = bitcast i64* %17 to i8*
  %62 = add i64 %28, 14
  %63 = inttoptr i64 %62 to i8*
  store i8 0, i8* %63, align 1
  call void @llvm.lifetime.start.p0i8(i64 8, i8* %61) #3
  %64 = ptrtoint i64* %17 to i64
  br label %65

65:                                               ; preds = %if.end
  %66 = lshr i64 %64, 3
  %67 = add i64 %66, 2147450880
  %68 = inttoptr i64 %67 to i8*
  %69 = load i8, i8* %68, align 1
  %70 = icmp ne i8 %69, 0
  br i1 %70, label %71, label %73

71:                                               ; preds = %65
  call void @__asan_report_store8(i64 %64) #8
  br label %72

72:                                               ; preds = %71
  unreachable

73:                                               ; preds = %65
  store i64 0, i64* %17, align 8
  %74 = bitcast i64* %17 to i8*
  %75 = load i8, i8* inttoptr (i64 add (i64 lshr (i64 ptrtoint (%struct._IO_FILE** @stdin to i64), i64 3), i64 2147450880) to i8*), align 1
  br label %76

76:                                               ; preds = %73
  %77 = icmp ne i8 %75, 0
  br i1 %77, label %78, label %80

78:                                               ; preds = %76
  call void @__asan_report_load8(i64 ptrtoint (%struct._IO_FILE** @stdin to i64)) #8
  br label %79

79:                                               ; preds = %78
  unreachable

80:                                               ; preds = %76
  %81 = load %struct._IO_FILE*, %struct._IO_FILE** @stdin, align 8
  %call9 = call i64 @fread(i8* %74, i64 8, i64 1, %struct._IO_FILE* %81)
  %82 = ptrtoint i64* %17 to i64
  %83 = lshr i64 %82, 3
  %84 = add i64 %83, 2147450880
  br label %85

85:                                               ; preds = %80
  %86 = inttoptr i64 %84 to i8*
  %87 = load i8, i8* %86, align 1
  %88 = icmp ne i8 %87, 0
  br i1 %88, label %89, label %91

89:                                               ; preds = %85
  call void @__asan_report_load8(i64 %82) #8
  br label %90

90:                                               ; preds = %89
  unreachable

91:                                               ; preds = %85
  %92 = load i64, i64* %17, align 8
  call void @__sanitizer_cov_trace_const_cmp8(i64 -3819410105351357762, i64 %92)
  br label %93

93:                                               ; preds = %91
  %cmp10 = icmp ne i64 %92, -3819410105351357762
  br i1 %cmp10, label %if.then11, label %if.end12

if.then11:                                        ; preds = %93
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([8 x i32]* @__sancov_gen_.4 to i64), i64 16) to i32*)) #8
  store i32 1, i32* %retval, align 4
  br label %94

94:                                               ; preds = %if.then11
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup20

if.end12:                                         ; preds = %93
  %95 = bitcast i32* %19 to i8*
  %96 = add i64 %28, 18
  %97 = inttoptr i64 %96 to i8*
  store i8 4, i8* %97, align 1
  call void @llvm.lifetime.start.p0i8(i64 4, i8* %95) #3
  %98 = ptrtoint i32* %19 to i64
  br label %99

99:                                               ; preds = %if.end12
  %100 = lshr i64 %98, 3
  %101 = add i64 %100, 2147450880
  %102 = inttoptr i64 %101 to i8*
  %103 = load i8, i8* %102, align 1
  %104 = icmp ne i8 %103, 0
  br i1 %104, label %105, label %113, !prof !15

105:                                              ; preds = %99
  %106 = and i64 %98, 7
  %107 = add i64 %106, 3
  %108 = trunc i64 %107 to i8
  br label %109

109:                                              ; preds = %105
  %110 = icmp sge i8 %108, %103
  br i1 %110, label %111, label %113

111:                                              ; preds = %109
  call void @__asan_report_store4(i64 %98) #8
  br label %112

112:                                              ; preds = %111
  unreachable

113:                                              ; preds = %109, %99
  store i32 0, i32* %19, align 4
  %114 = bitcast i32* %19 to i8*
  %115 = load i8, i8* inttoptr (i64 add (i64 lshr (i64 ptrtoint (%struct._IO_FILE** @stdin to i64), i64 3), i64 2147450880) to i8*), align 1
  br label %116

116:                                              ; preds = %113
  %117 = icmp ne i8 %115, 0
  br i1 %117, label %118, label %120

118:                                              ; preds = %116
  call void @__asan_report_load8(i64 ptrtoint (%struct._IO_FILE** @stdin to i64)) #8
  br label %119

119:                                              ; preds = %118
  unreachable

120:                                              ; preds = %116
  %121 = load %struct._IO_FILE*, %struct._IO_FILE** @stdin, align 8
  %call13 = call i64 @fread(i8* %114, i64 4, i64 1, %struct._IO_FILE* %121)
  %122 = ptrtoint i32* %19 to i64
  %123 = lshr i64 %122, 3
  %124 = add i64 %123, 2147450880
  br label %125

125:                                              ; preds = %120
  %126 = inttoptr i64 %124 to i8*
  %127 = load i8, i8* %126, align 1
  %128 = icmp ne i8 %127, 0
  br i1 %128, label %129, label %137, !prof !15

129:                                              ; preds = %125
  %130 = and i64 %122, 7
  %131 = add i64 %130, 3
  %132 = trunc i64 %131 to i8
  br label %133

133:                                              ; preds = %129
  %134 = icmp sge i8 %132, %127
  br i1 %134, label %135, label %137

135:                                              ; preds = %133
  call void @__asan_report_load4(i64 %122) #8
  br label %136

136:                                              ; preds = %135
  unreachable

137:                                              ; preds = %133, %125
  %138 = load i32, i32* %19, align 4
  call void @__sanitizer_cov_trace_const_cmp4(i32 -559038242, i32 %138)
  br label %139

139:                                              ; preds = %137
  %cmp14 = icmp ne i32 %138, -559038242
  br i1 %cmp14, label %if.then15, label %if.end16

if.then15:                                        ; preds = %139
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([8 x i32]* @__sancov_gen_.4 to i64), i64 20) to i32*)) #8
  store i32 1, i32* %retval, align 4
  br label %140

140:                                              ; preds = %if.then15
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup19

if.end16:                                         ; preds = %139
  %141 = bitcast i16* %21 to i8*
  %142 = add i64 %28, 20
  %143 = inttoptr i64 %142 to i8*
  store i8 2, i8* %143, align 1
  call void @llvm.lifetime.start.p0i8(i64 2, i8* %141) #3
  %144 = ptrtoint i16* %21 to i64
  br label %145

145:                                              ; preds = %if.end16
  %146 = lshr i64 %144, 3
  %147 = add i64 %146, 2147450880
  %148 = inttoptr i64 %147 to i8*
  %149 = load i8, i8* %148, align 1
  %150 = icmp ne i8 %149, 0
  br i1 %150, label %151, label %159, !prof !15

151:                                              ; preds = %145
  %152 = and i64 %144, 7
  %153 = add i64 %152, 1
  %154 = trunc i64 %153 to i8
  br label %155

155:                                              ; preds = %151
  %156 = icmp sge i8 %154, %149
  br i1 %156, label %157, label %159

157:                                              ; preds = %155
  call void @__asan_report_store2(i64 %144) #8
  br label %158

158:                                              ; preds = %157
  unreachable

159:                                              ; preds = %155, %145
  store i16 0, i16* %21, align 2
  %160 = bitcast i16* %21 to i8*
  %161 = load i8, i8* inttoptr (i64 add (i64 lshr (i64 ptrtoint (%struct._IO_FILE** @stdin to i64), i64 3), i64 2147450880) to i8*), align 1
  br label %162

162:                                              ; preds = %159
  %163 = icmp ne i8 %161, 0
  br i1 %163, label %164, label %166

164:                                              ; preds = %162
  call void @__asan_report_load8(i64 ptrtoint (%struct._IO_FILE** @stdin to i64)) #8
  br label %165

165:                                              ; preds = %164
  unreachable

166:                                              ; preds = %162
  %167 = load %struct._IO_FILE*, %struct._IO_FILE** @stdin, align 8
  %call17 = call i64 @fread(i8* %160, i64 2, i64 1, %struct._IO_FILE* %167)
  %168 = ptrtoint i16* %21 to i64
  %169 = lshr i64 %168, 3
  %170 = add i64 %169, 2147450880
  br label %171

171:                                              ; preds = %166
  %172 = inttoptr i64 %170 to i8*
  %173 = load i8, i8* %172, align 1
  %174 = icmp ne i8 %173, 0
  br i1 %174, label %175, label %183, !prof !15

175:                                              ; preds = %171
  %176 = and i64 %168, 7
  %177 = add i64 %176, 1
  %178 = trunc i64 %177 to i8
  br label %179

179:                                              ; preds = %175
  %180 = icmp sge i8 %178, %173
  br i1 %180, label %181, label %183

181:                                              ; preds = %179
  call void @__asan_report_load2(i64 %168) #8
  br label %182

182:                                              ; preds = %181
  unreachable

183:                                              ; preds = %179, %171
  %184 = load i16, i16* %21, align 2
  %conv = zext i16 %184 to i32
  %185 = zext i32 %conv to i64
  br label %186

186:                                              ; preds = %183
  call void @__sanitizer_cov_trace_switch(i64 %185, i64* getelementptr inbounds ([3 x i64], [3 x i64]* @__sancov_gen_cov_switch_values, i32 0, i32 0))
  switch i32 %conv, label %sw.default [
    i32 48879, label %sw.bb
  ]

sw.bb:                                            ; preds = %186
  br label %sw.epilog

sw.default:                                       ; preds = %186
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([8 x i32]* @__sancov_gen_.4 to i64), i64 24) to i32*)) #8
  store i32 1, i32* %retval, align 4
  br label %187

187:                                              ; preds = %sw.default
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup

sw.epilog:                                        ; preds = %sw.bb
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([8 x i32]* @__sancov_gen_.4 to i64), i64 28) to i32*)) #8
  %call18 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ({ [26 x i8], [38 x i8] }, { [26 x i8], [38 x i8] }* @.str.3, i32 0, i32 0, i64 0))
  store i32 0, i32* %retval, align 4
  br label %188

188:                                              ; preds = %sw.epilog
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup

cleanup:                                          ; preds = %188, %187
  %189 = bitcast i16* %21 to i8*
  %190 = add i64 %28, 20
  %191 = inttoptr i64 %190 to i8*
  br label %192

192:                                              ; preds = %cleanup
  store i8 -8, i8* %191, align 1
  call void @llvm.lifetime.end.p0i8(i64 2, i8* %189) #3
  br label %cleanup19

cleanup19:                                        ; preds = %192, %140
  %193 = bitcast i32* %19 to i8*
  %194 = add i64 %28, 18
  %195 = inttoptr i64 %194 to i8*
  br label %196

196:                                              ; preds = %cleanup19
  store i8 -8, i8* %195, align 1
  call void @llvm.lifetime.end.p0i8(i64 4, i8* %193) #3
  br label %cleanup20

cleanup20:                                        ; preds = %196, %94
  %197 = bitcast i64* %17 to i8*
  %198 = add i64 %28, 14
  %199 = inttoptr i64 %198 to i8*
  br label %200

200:                                              ; preds = %cleanup20
  store i8 -8, i8* %199, align 1
  call void @llvm.lifetime.end.p0i8(i64 8, i8* %197) #3
  br label %cleanup21

cleanup21:                                        ; preds = %200, %60
  %201 = bitcast [44 x i8]* %15 to i8*
  %202 = add i64 %28, 4
  %203 = inttoptr i64 %202 to i32*
  store i32 -117901064, i32* %203, align 1
  %204 = add i64 %28, 8
  %205 = inttoptr i64 %204 to i16*
  br label %206

206:                                              ; preds = %cleanup21
  store i16 -1800, i16* %205, align 1
  call void @llvm.lifetime.end.p0i8(i64 44, i8* %201) #3
  %207 = load i32, i32* %retval, align 4
  store i64 1172321806, i64* %22, align 8
  %208 = icmp ne i64 %7, 0
  br i1 %208, label %209, label %223

209:                                              ; preds = %206
  %210 = add i64 %28, 0
  %211 = inttoptr i64 %210 to i64*
  store i64 -723401728380766731, i64* %211, align 1
  %212 = add i64 %28, 8
  %213 = inttoptr i64 %212 to i64*
  store i64 -723401728380766731, i64* %213, align 1
  %214 = add i64 %28, 16
  %215 = inttoptr i64 %214 to i64*
  store i64 -723401728380766731, i64* %215, align 1
  br label %216

216:                                              ; preds = %209
  %217 = add i64 %28, 24
  %218 = inttoptr i64 %217 to i64*
  store i64 -723401728380766731, i64* %218, align 1
  %219 = add i64 %7, 248
  %220 = inttoptr i64 %219 to i64*
  %221 = load i64, i64* %220, align 8
  %222 = inttoptr i64 %221 to i8*
  store i8 0, i8* %222, align 1
  br label %231

223:                                              ; preds = %206
  %224 = add i64 %28, 0
  %225 = inttoptr i64 %224 to i64*
  store i64 0, i64* %225, align 1
  %226 = add i64 %28, 8
  %227 = inttoptr i64 %226 to i64*
  br label %228

228:                                              ; preds = %223
  store i64 0, i64* %227, align 1
  %229 = add i64 %28, 16
  %230 = inttoptr i64 %229 to i64*
  store i64 0, i64* %230, align 1
  br label %231

231:                                              ; preds = %228, %216
  ret i32 %207
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
  br label %0

0:                                                ; preds = %entry
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
  br label %1

1:                                                ; preds = %0
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
  br label %1

1:                                                ; preds = %0
  call void @__asan_register_globals(i64 ptrtoint ([5 x { i64, i64, i64, i64, i64, i64, i64, i64 }]* @0 to i64), i64 5)
  ret void
}

declare void @__asan_version_mismatch_check_v8()

define internal void @asan.module_dtor() {
  call void @__asan_unregister_globals(i64 ptrtoint ([5 x { i64, i64, i64, i64, i64, i64, i64, i64 }]* @0 to i64), i64 5)
  br label %1

1:                                                ; preds = %0
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
