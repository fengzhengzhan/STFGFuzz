; ModuleID = 'IR/demo.ll'
source_filename = "demo/demo.cc"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

%"class.std::ios_base::Init" = type { i8 }
%struct.option = type { i8*, i32, i32*, i32 }
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
@_ZZ4mainE12long_options = internal global { [1 x %struct.option], [32 x i8] } { [1 x %struct.option] [%struct.option { i8* getelementptr inbounds ({ [5 x i8], [59 x i8] }, { [5 x i8], [59 x i8] }* @.str, i32 0, i32 0, i32 0), i32 1, i32* null, i32 102 }], [32 x i8] zeroinitializer }, align 32
@.str = internal constant { [5 x i8], [59 x i8] } { [5 x i8] c"file\00", [59 x i8] zeroinitializer }, align 32
@.str.1 = internal constant { [3 x i8], [61 x i8] } { [3 x i8] c"f:\00", [61 x i8] zeroinitializer }, align 32
@optarg = external dso_local global i8*, align 8
@.str.2 = internal constant { [18 x i8], [46 x i8] } { [18 x i8] c"Error Parameters!\00", [46 x i8] zeroinitializer }, align 32
@.str.3 = internal constant { [2 x i8], [62 x i8] } { [2 x i8] c"r\00", [62 x i8] zeroinitializer }, align 32
@.str.4 = internal constant { [21 x i8], [43 x i8] } { [21 x i8] c"The quick brown fox \00", [43 x i8] zeroinitializer }, align 32
@.str.5 = internal constant { [12 x i8], [52 x i8] } { [12 x i8] c"jumps over \00", [52 x i8] zeroinitializer }, align 32
@.str.6 = internal constant { [14 x i8], [50 x i8] } { [14 x i8] c"the lazy dog.\00", [50 x i8] zeroinitializer }, align 32
@.str.7 = internal constant { [27 x i8], [37 x i8] } { [27 x i8] c"Though first str/mem Cmp.\0A\00", [37 x i8] zeroinitializer }, align 32
@.str.8 = internal constant { [4 x i8], [60 x i8] } { [4 x i8] c"%s\0A\00", [60 x i8] zeroinitializer }, align 32
@.str.9 = internal constant { [33 x i8], [63 x i8] } { [33 x i8] c"Puzzle solved, Congratulations!\0A\00", [63 x i8] zeroinitializer }, align 32
@__sancov_lowest_stack = external thread_local(initialexec) global i64
@__sancov_gen_ = private global [1 x i32] zeroinitializer, section "__sancov_guards", comdat($"__cxx_global_var_init$21576b91ab9b15712202e1b4a494877f"), align 4, !associated !0
@__sancov_gen_.10 = private global [15 x i32] zeroinitializer, section "__sancov_guards", comdat($main), align 4, !associated !1
@__sancov_gen_cov_switch_values = internal global [3 x i64] [i64 1, i64 32, i64 102]
@__sancov_gen_cov_switch_values.11 = internal global [5 x i64] [i64 3, i64 32, i64 48879, i64 61374, i64 65259]
@__sancov_gen_.12 = private global [1 x i32] zeroinitializer, section "__sancov_guards", comdat($"_GLOBAL__sub_I_demo.cc$21576b91ab9b15712202e1b4a494877f"), align 4, !associated !2
@__start___sancov_guards = external hidden global i32
@__stop___sancov_guards = external hidden global i32
@__asan_option_detect_stack_use_after_return = external global i32
@___asan_gen_ = private unnamed_addr constant [87 x i8] c"6 32 4 9 opt_index 48 201 3 str 320 45 6 buffer 400 201 2 s1 672 201 2 s2 944 201 2 s3\00", align 1
@___asan_gen_.13 = private constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.14 = private unnamed_addr constant [14 x i8] c"std::__ioinit\00", align 1
@___asan_gen_.15 = private unnamed_addr constant [67 x i8] c"/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/iostream\00", align 1
@___asan_gen_.16 = private unnamed_addr constant { [67 x i8]*, i32, i32 } { [67 x i8]* @___asan_gen_.15, i32 74, i32 25 }
@___asan_gen_.17 = private unnamed_addr constant [13 x i8] c"long_options\00", align 1
@___asan_gen_.18 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.19 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.18, i32 18, i32 26 }
@___asan_gen_.20 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.21 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.22 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.21, i32 20, i32 10 }
@___asan_gen_.23 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.24 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.25 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.24, i32 22, i32 42 }
@___asan_gen_.26 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.27 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.28 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.27, i32 31, i32 20 }
@___asan_gen_.29 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.30 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.31 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.30, i32 39, i32 32 }
@___asan_gen_.32 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.33 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.34 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.33, i32 52, i32 28 }
@___asan_gen_.35 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.36 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.37 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.36, i32 53, i32 30 }
@___asan_gen_.38 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.39 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.40 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.39, i32 54, i32 29 }
@___asan_gen_.41 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.42 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.43 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.42, i32 58, i32 12 }
@___asan_gen_.44 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.45 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.46 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.45, i32 73, i32 12 }
@___asan_gen_.47 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.48 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.49 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.48, i32 101, i32 12 }
@llvm.compiler.used = appending global [15 x i8*] [i8* bitcast ([1 x i32]* @__sancov_gen_ to i8*), i8* bitcast ([15 x i32]* @__sancov_gen_.10 to i8*), i8* bitcast ([1 x i32]* @__sancov_gen_.12 to i8*), i8* getelementptr inbounds ({ %"class.std::ios_base::Init", [63 x i8] }, { %"class.std::ios_base::Init", [63 x i8] }* @_ZStL8__ioinit, i32 0, i32 0, i32 0), i8* bitcast ({ [1 x %struct.option], [32 x i8] }* @_ZZ4mainE12long_options to i8*), i8* getelementptr inbounds ({ [5 x i8], [59 x i8] }, { [5 x i8], [59 x i8] }* @.str, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [3 x i8], [61 x i8] }, { [3 x i8], [61 x i8] }* @.str.1, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [18 x i8], [46 x i8] }, { [18 x i8], [46 x i8] }* @.str.2, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [2 x i8], [62 x i8] }, { [2 x i8], [62 x i8] }* @.str.3, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [21 x i8], [43 x i8] }, { [21 x i8], [43 x i8] }* @.str.4, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [12 x i8], [52 x i8] }, { [12 x i8], [52 x i8] }* @.str.5, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [14 x i8], [50 x i8] }, { [14 x i8], [50 x i8] }* @.str.6, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [27 x i8], [37 x i8] }, { [27 x i8], [37 x i8] }* @.str.7, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [4 x i8], [60 x i8] }, { [4 x i8], [60 x i8] }* @.str.8, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [33 x i8], [63 x i8] }, { [33 x i8], [63 x i8] }* @.str.9, i32 0, i32 0, i32 0)], section "llvm.metadata"
@0 = internal global [12 x { i64, i64, i64, i64, i64, i64, i64, i64 }] [{ i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ %"class.std::ios_base::Init", [63 x i8] }* @_ZStL8__ioinit to i64), i64 1, i64 64, i64 ptrtoint ([14 x i8]* @___asan_gen_.14 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.13 to i64), i64 1, i64 ptrtoint ({ [67 x i8]*, i32, i32 }* @___asan_gen_.16 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [1 x %struct.option], [32 x i8] }* @_ZZ4mainE12long_options to i64), i64 32, i64 64, i64 ptrtoint ([13 x i8]* @___asan_gen_.17 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.13 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.19 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [5 x i8], [59 x i8] }* @.str to i64), i64 5, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.20 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.13 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.22 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [3 x i8], [61 x i8] }* @.str.1 to i64), i64 3, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.23 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.13 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.25 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [18 x i8], [46 x i8] }* @.str.2 to i64), i64 18, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.26 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.13 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.28 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [2 x i8], [62 x i8] }* @.str.3 to i64), i64 2, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.29 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.13 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.31 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [21 x i8], [43 x i8] }* @.str.4 to i64), i64 21, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.32 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.13 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.34 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [12 x i8], [52 x i8] }* @.str.5 to i64), i64 12, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.35 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.13 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.37 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [14 x i8], [50 x i8] }* @.str.6 to i64), i64 14, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.38 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.13 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.40 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [27 x i8], [37 x i8] }* @.str.7 to i64), i64 27, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.41 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.13 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.43 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [4 x i8], [60 x i8] }* @.str.8 to i64), i64 4, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.44 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.13 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.46 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [33 x i8], [63 x i8] }* @.str.9 to i64), i64 33, i64 96, i64 ptrtoint ([17 x i8]* @___asan_gen_.47 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.13 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.49 to i64), i64 -1 }]
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
  %opt = alloca i32, align 4
  %filename = alloca i8*, align 8
  %fp = alloca %struct._IO_FILE*, align 8
  %cleanup.dest.slot = alloca i32, align 4
  %i = alloca i32, align 4
  %i22 = alloca i32, align 4
  br label %0

0:                                                ; preds = %entry
  %i37 = alloca i32, align 4
  %x = alloca i64, align 8
  %y = alloca i32, align 4
  %z = alloca i16, align 2
  %asan_local_stack_base = alloca i64, align 8
  %1 = load i32, i32* @__asan_option_detect_stack_use_after_return, align 4
  %2 = icmp ne i32 %1, 0
  br i1 %2, label %3, label %6

3:                                                ; preds = %0
  %4 = call i64 @__asan_stack_malloc_5(i64 1216)
  br label %5

5:                                                ; preds = %3
  br label %6

6:                                                ; preds = %5, %0
  %7 = phi i64 [ 0, %0 ], [ %4, %5 ]
  %8 = icmp eq i64 %7, 0
  br i1 %8, label %9, label %12

9:                                                ; preds = %6
  %MyAlloca = alloca i8, i64 1216, align 32
  %10 = ptrtoint i8* %MyAlloca to i64
  br label %11

11:                                               ; preds = %9
  br label %12

12:                                               ; preds = %11, %6
  %13 = phi i64 [ %7, %6 ], [ %10, %11 ]
  store i64 %13, i64* %asan_local_stack_base, align 8
  %14 = add i64 %13, 32
  %15 = inttoptr i64 %14 to i32*
  %16 = add i64 %13, 48
  %17 = inttoptr i64 %16 to [201 x i8]*
  %18 = add i64 %13, 320
  %19 = inttoptr i64 %18 to [45 x i8]*
  %20 = add i64 %13, 400
  %21 = inttoptr i64 %20 to [201 x i8]*
  %22 = add i64 %13, 672
  %23 = inttoptr i64 %22 to [201 x i8]*
  %24 = add i64 %13, 944
  %25 = inttoptr i64 %24 to [201 x i8]*
  %26 = inttoptr i64 %13 to i64*
  store i64 1102416563, i64* %26, align 8
  %27 = add i64 %13, 8
  %28 = inttoptr i64 %27 to i64*
  store i64 ptrtoint ([87 x i8]* @___asan_gen_ to i64), i64* %28, align 8
  %29 = add i64 %13, 16
  %30 = inttoptr i64 %29 to i64*
  store i64 ptrtoint (i32 (i32, i8**)* @main to i64), i64* %30, align 8
  %31 = lshr i64 %13, 3
  %32 = add i64 %31, 2147450880
  %33 = add i64 %32, 0
  %34 = inttoptr i64 %33 to i64*
  store i64 -506387807054204431, i64* %34, align 1
  %35 = add i64 %32, 8
  %36 = inttoptr i64 %35 to i64*
  store i64 -506381209866536712, i64* %36, align 1
  %37 = add i64 %32, 16
  %38 = inttoptr i64 %37 to i64*
  store i64 -506381209866536712, i64* %38, align 1
  %39 = add i64 %32, 24
  %40 = inttoptr i64 %39 to i64*
  store i64 -506381209866536712, i64* %40, align 1
  %41 = add i64 %32, 32
  %42 = inttoptr i64 %41 to i64*
  store i64 -940422246894996750, i64* %42, align 1
  %43 = add i64 %32, 40
  %44 = inttoptr i64 %43 to i64*
  store i64 -940415623954368264, i64* %44, align 1
  %45 = add i64 %32, 48
  %46 = inttoptr i64 %45 to i64*
  store i64 -506381209866538254, i64* %46, align 1
  %47 = add i64 %32, 56
  %48 = inttoptr i64 %47 to i64*
  store i64 -506381209866536712, i64* %48, align 1
  %49 = add i64 %32, 64
  %50 = inttoptr i64 %49 to i64*
  store i64 -506381209866536712, i64* %50, align 1
  %51 = add i64 %32, 72
  %52 = inttoptr i64 %51 to i64*
  store i64 -940422246793938696, i64* %52, align 1
  %53 = add i64 %32, 80
  %54 = inttoptr i64 %53 to i64*
  store i64 -506381209967594766, i64* %54, align 1
  %55 = add i64 %32, 88
  %56 = inttoptr i64 %55 to i64*
  store i64 -506381209866536712, i64* %56, align 1
  %57 = add i64 %32, 96
  %58 = inttoptr i64 %57 to i64*
  store i64 -506381209866536712, i64* %58, align 1
  %59 = add i64 %32, 104
  %60 = inttoptr i64 %59 to i64*
  store i64 -940415623954368264, i64* %60, align 1
  %61 = add i64 %32, 112
  %62 = inttoptr i64 %61 to i64*
  store i64 -506387832807165198, i64* %62, align 1
  %63 = add i64 %32, 120
  %64 = inttoptr i64 %63 to i64*
  store i64 -506381209866536712, i64* %64, align 1
  %65 = add i64 %32, 128
  %66 = inttoptr i64 %65 to i64*
  store i64 -506381209866536712, i64* %66, align 1
  %67 = add i64 %32, 136
  %68 = inttoptr i64 %67 to i64*
  store i64 -506381209866536712, i64* %68, align 1
  %69 = add i64 %32, 144
  %70 = inttoptr i64 %69 to i64*
  store i64 -868082074056920077, i64* %70, align 1
  call void @__sanitizer_cov_trace_pc_guard(i32* getelementptr inbounds ([15 x i32], [15 x i32]* @__sancov_gen_.10, i32 0, i32 0)) #8
  store i32 0, i32* %retval, align 4
  store i32 %argc, i32* %argc.addr, align 4
  store i8** %argv, i8*** %argv.addr, align 8
  %71 = bitcast i32* %opt to i8*
  call void @llvm.lifetime.start.p0i8(i64 4, i8* %71) #3
  %72 = bitcast i32* %15 to i8*
  %73 = add i64 %32, 4
  %74 = inttoptr i64 %73 to i8*
  store i8 4, i8* %74, align 1
  call void @llvm.lifetime.start.p0i8(i64 4, i8* %72) #3
  %75 = bitcast i8** %filename to i8*
  call void @llvm.lifetime.start.p0i8(i64 8, i8* %75) #3
  br label %while.cond

while.cond:                                       ; preds = %sw.epilog, %12
  %76 = load i32, i32* %argc.addr, align 4
  %77 = load i8**, i8*** %argv.addr, align 8
  %call = call i32 @getopt_long(i32 %76, i8** %77, i8* getelementptr inbounds ({ [3 x i8], [61 x i8] }, { [3 x i8], [61 x i8] }* @.str.1, i32 0, i32 0, i64 0), %struct.option* getelementptr inbounds ({ [1 x %struct.option], [32 x i8] }, { [1 x %struct.option], [32 x i8] }* @_ZZ4mainE12long_options, i32 0, i32 0, i64 0), i32* %15) #3
  store i32 %call, i32* %opt, align 4
  br label %78

78:                                               ; preds = %while.cond
  call void @__sanitizer_cov_trace_const_cmp4(i32 -1, i32 %call)
  %cmp = icmp ne i32 %call, -1
  br i1 %cmp, label %while.body, label %while.end

while.body:                                       ; preds = %78
  %79 = load i32, i32* %opt, align 4
  %80 = zext i32 %79 to i64
  br label %81

81:                                               ; preds = %while.body
  call void @__sanitizer_cov_trace_switch(i64 %80, i64* getelementptr inbounds ([3 x i64], [3 x i64]* @__sancov_gen_cov_switch_values, i32 0, i32 0))
  switch i32 %79, label %sw.default [
    i32 102, label %sw.bb
  ]

sw.bb:                                            ; preds = %81
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([15 x i32]* @__sancov_gen_.10 to i64), i64 4) to i32*)) #8
  %82 = load i8, i8* inttoptr (i64 add (i64 lshr (i64 ptrtoint (i8** @optarg to i64), i64 3), i64 2147450880) to i8*), align 1
  br label %83

83:                                               ; preds = %sw.bb
  %84 = icmp ne i8 %82, 0
  br i1 %84, label %85, label %87

85:                                               ; preds = %83
  call void @__asan_report_load8(i64 ptrtoint (i8** @optarg to i64)) #8
  br label %86

86:                                               ; preds = %85
  unreachable

87:                                               ; preds = %83
  %88 = load i8*, i8** @optarg, align 8
  store i8* %88, i8** %filename, align 8
  br label %89

89:                                               ; preds = %87
  br label %sw.epilog

sw.default:                                       ; preds = %81
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([15 x i32]* @__sancov_gen_.10 to i64), i64 8) to i32*)) #8
  %call1 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ({ [18 x i8], [46 x i8] }, { [18 x i8], [46 x i8] }* @.str.2, i32 0, i32 0, i64 0))
  br label %90

90:                                               ; preds = %sw.default
  br label %sw.epilog

sw.epilog:                                        ; preds = %90, %89
  br label %while.cond, !llvm.loop !29

while.end:                                        ; preds = %78
  %91 = bitcast [201 x i8]* %17 to i8*
  %92 = add i64 %32, 6
  %93 = inttoptr i64 %92 to i64*
  store i64 0, i64* %93, align 1
  %94 = add i64 %32, 14
  %95 = inttoptr i64 %94 to i64*
  store i64 0, i64* %95, align 1
  %96 = add i64 %32, 22
  %97 = inttoptr i64 %96 to i64*
  store i64 0, i64* %97, align 1
  %98 = add i64 %32, 30
  %99 = inttoptr i64 %98 to i16*
  store i16 256, i16* %99, align 1
  call void @llvm.lifetime.start.p0i8(i64 201, i8* %91) #3
  %100 = bitcast %struct._IO_FILE** %fp to i8*
  call void @llvm.lifetime.start.p0i8(i64 8, i8* %100) #3
  %101 = load i8*, i8** %filename, align 8
  %call2 = call %struct._IO_FILE* @fopen(i8* %101, i8* getelementptr inbounds ({ [2 x i8], [62 x i8] }, { [2 x i8], [62 x i8] }* @.str.3, i32 0, i32 0, i64 0))
  store %struct._IO_FILE* %call2, %struct._IO_FILE** %fp, align 8
  %arraydecay = getelementptr inbounds [201 x i8], [201 x i8]* %17, i64 0, i64 0
  %102 = load %struct._IO_FILE*, %struct._IO_FILE** %fp, align 8
  %call3 = call i8* @fgets(i8* %arraydecay, i32 201, %struct._IO_FILE* %102)
  br label %103

103:                                              ; preds = %while.end
  %104 = bitcast [45 x i8]* %19 to i8*
  %105 = add i64 %32, 40
  %106 = inttoptr i64 %105 to i32*
  store i32 0, i32* %106, align 1
  %107 = add i64 %32, 44
  %108 = inttoptr i64 %107 to i16*
  store i16 1280, i16* %108, align 1
  call void @llvm.lifetime.start.p0i8(i64 45, i8* %104) #3
  %109 = bitcast [45 x i8]* %19 to i8*
  %110 = call i8* @__asan_memset(i8* %109, i32 0, i64 45)
  %arraydecay4 = getelementptr inbounds [45 x i8], [45 x i8]* %19, i64 0, i64 0
  %arraydecay5 = getelementptr inbounds [201 x i8], [201 x i8]* %17, i64 0, i64 0
  %111 = call i8* @__asan_memcpy(i8* %arraydecay4, i8* %arraydecay5, i64 44)
  %arrayidx = getelementptr inbounds [45 x i8], [45 x i8]* %19, i64 0, i64 44
  %112 = ptrtoint i8* %arrayidx to i64
  %113 = lshr i64 %112, 3
  %114 = add i64 %113, 2147450880
  %115 = inttoptr i64 %114 to i8*
  %116 = load i8, i8* %115, align 1
  %117 = icmp ne i8 %116, 0
  br i1 %117, label %118, label %125, !prof !31

118:                                              ; preds = %103
  %119 = and i64 %112, 7
  %120 = trunc i64 %119 to i8
  br label %121

121:                                              ; preds = %118
  %122 = icmp sge i8 %120, %116
  br i1 %122, label %123, label %125

123:                                              ; preds = %121
  call void @__asan_report_store1(i64 %112) #8
  br label %124

124:                                              ; preds = %123
  unreachable

125:                                              ; preds = %121, %103
  store i8 0, i8* %arrayidx, align 4
  %arrayidx6 = getelementptr inbounds [45 x i8], [45 x i8]* %19, i64 0, i64 0
  %call7 = call i32 @memcmp(i8* %arrayidx6, i8* getelementptr inbounds ({ [21 x i8], [43 x i8] }, { [21 x i8], [43 x i8] }* @.str.4, i32 0, i32 0, i64 0), i64 20) #9
  br label %126

126:                                              ; preds = %125
  call void @__sanitizer_cov_trace_const_cmp4(i32 0, i32 %call7)
  %cmp8 = icmp ne i32 %call7, 0
  br i1 %cmp8, label %while.end.if.then_crit_edge, label %lor.lhs.false

while.end.if.then_crit_edge:                      ; preds = %126
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([15 x i32]* @__sancov_gen_.10 to i64), i64 12) to i32*)) #8
  br label %127

127:                                              ; preds = %while.end.if.then_crit_edge
  br label %if.then

lor.lhs.false:                                    ; preds = %126
  %arrayidx9 = getelementptr inbounds [45 x i8], [45 x i8]* %19, i64 0, i64 20
  %call10 = call i32 @strncmp(i8* %arrayidx9, i8* getelementptr inbounds ({ [12 x i8], [52 x i8] }, { [12 x i8], [52 x i8] }* @.str.5, i32 0, i32 0, i64 0), i64 11) #10
  call void @__sanitizer_cov_trace_const_cmp4(i32 0, i32 %call10)
  br label %128

128:                                              ; preds = %lor.lhs.false
  %cmp11 = icmp ne i32 %call10, 0
  br i1 %cmp11, label %lor.lhs.false.if.then_crit_edge, label %lor.lhs.false12

lor.lhs.false.if.then_crit_edge:                  ; preds = %128
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([15 x i32]* @__sancov_gen_.10 to i64), i64 16) to i32*)) #8
  br label %129

129:                                              ; preds = %lor.lhs.false.if.then_crit_edge
  br label %if.then

lor.lhs.false12:                                  ; preds = %128
  %arrayidx13 = getelementptr inbounds [45 x i8], [45 x i8]* %19, i64 0, i64 31
  %call14 = call i32 @strcmp(i8* %arrayidx13, i8* getelementptr inbounds ({ [14 x i8], [50 x i8] }, { [14 x i8], [50 x i8] }* @.str.6, i32 0, i32 0, i64 0)) #9
  call void @__sanitizer_cov_trace_const_cmp4(i32 0, i32 %call14)
  br label %130

130:                                              ; preds = %lor.lhs.false12
  %cmp15 = icmp ne i32 %call14, 0
  br i1 %cmp15, label %lor.lhs.false12.if.then_crit_edge, label %if.end

lor.lhs.false12.if.then_crit_edge:                ; preds = %130
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([15 x i32]* @__sancov_gen_.10 to i64), i64 20) to i32*)) #8
  br label %131

131:                                              ; preds = %lor.lhs.false12.if.then_crit_edge
  br label %if.then

if.then:                                          ; preds = %131, %129, %127
  store i32 1, i32* %retval, align 4
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %132

132:                                              ; preds = %if.then
  br label %cleanup80

if.end:                                           ; preds = %130
  %call16 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ({ [27 x i8], [37 x i8] }, { [27 x i8], [37 x i8] }* @.str.7, i32 0, i32 0, i64 0))
  %133 = bitcast [201 x i8]* %21 to i8*
  %134 = add i64 %32, 50
  %135 = inttoptr i64 %134 to i64*
  store i64 0, i64* %135, align 1
  %136 = add i64 %32, 58
  %137 = inttoptr i64 %136 to i64*
  store i64 0, i64* %137, align 1
  %138 = add i64 %32, 66
  %139 = inttoptr i64 %138 to i64*
  store i64 0, i64* %139, align 1
  %140 = add i64 %32, 74
  %141 = inttoptr i64 %140 to i16*
  store i16 256, i16* %141, align 1
  call void @llvm.lifetime.start.p0i8(i64 201, i8* %133) #3
  %142 = bitcast [201 x i8]* %23 to i8*
  %143 = add i64 %32, 84
  %144 = inttoptr i64 %143 to i64*
  store i64 0, i64* %144, align 1
  %145 = add i64 %32, 92
  %146 = inttoptr i64 %145 to i64*
  store i64 0, i64* %146, align 1
  %147 = add i64 %32, 100
  %148 = inttoptr i64 %147 to i64*
  br label %149

149:                                              ; preds = %if.end
  store i64 0, i64* %148, align 1
  %150 = add i64 %32, 108
  %151 = inttoptr i64 %150 to i16*
  store i16 256, i16* %151, align 1
  call void @llvm.lifetime.start.p0i8(i64 201, i8* %142) #3
  %152 = bitcast [201 x i8]* %25 to i8*
  %153 = add i64 %32, 118
  %154 = inttoptr i64 %153 to i64*
  store i64 0, i64* %154, align 1
  %155 = add i64 %32, 126
  %156 = inttoptr i64 %155 to i64*
  store i64 0, i64* %156, align 1
  %157 = add i64 %32, 134
  %158 = inttoptr i64 %157 to i64*
  store i64 0, i64* %158, align 1
  %159 = add i64 %32, 142
  %160 = inttoptr i64 %159 to i16*
  store i16 256, i16* %160, align 1
  call void @llvm.lifetime.start.p0i8(i64 201, i8* %152) #3
  %161 = bitcast i32* %i to i8*
  call void @llvm.lifetime.start.p0i8(i64 4, i8* %161) #3
  store i32 0, i32* %i, align 4
  br label %for.cond

for.cond:                                         ; preds = %201, %149
  %162 = load i32, i32* %i, align 4
  call void @__sanitizer_cov_trace_const_cmp4(i32 16, i32 %162)
  br label %163

163:                                              ; preds = %for.cond
  %cmp17 = icmp slt i32 %162, 16
  br i1 %cmp17, label %for.body, label %for.cond.cleanup

for.cond.cleanup:                                 ; preds = %163
  store i32 5, i32* %cleanup.dest.slot, align 4
  %164 = bitcast i32* %i to i8*
  br label %165

165:                                              ; preds = %for.cond.cleanup
  call void @llvm.lifetime.end.p0i8(i64 4, i8* %164) #3
  br label %for.end

for.body:                                         ; preds = %163
  %166 = load i32, i32* %i, align 4
  %add = add nsw i32 %166, 44
  %idxprom = sext i32 %add to i64
  %arrayidx18 = getelementptr inbounds [201 x i8], [201 x i8]* %17, i64 0, i64 %idxprom
  %167 = ptrtoint i8* %arrayidx18 to i64
  %168 = lshr i64 %167, 3
  br label %169

169:                                              ; preds = %for.body
  %170 = add i64 %168, 2147450880
  %171 = inttoptr i64 %170 to i8*
  %172 = load i8, i8* %171, align 1
  %173 = icmp ne i8 %172, 0
  br i1 %173, label %174, label %181, !prof !31

174:                                              ; preds = %169
  %175 = and i64 %167, 7
  %176 = trunc i64 %175 to i8
  br label %177

177:                                              ; preds = %174
  %178 = icmp sge i8 %176, %172
  br i1 %178, label %179, label %181

179:                                              ; preds = %177
  call void @__asan_report_load1(i64 %167) #8
  br label %180

180:                                              ; preds = %179
  unreachable

181:                                              ; preds = %177, %169
  %182 = load i8, i8* %arrayidx18, align 1
  %183 = load i32, i32* %i, align 4
  %idxprom19 = sext i32 %183 to i64
  %arrayidx20 = getelementptr inbounds [201 x i8], [201 x i8]* %21, i64 0, i64 %idxprom19
  %184 = ptrtoint i8* %arrayidx20 to i64
  %185 = lshr i64 %184, 3
  br label %186

186:                                              ; preds = %181
  %187 = add i64 %185, 2147450880
  %188 = inttoptr i64 %187 to i8*
  %189 = load i8, i8* %188, align 1
  %190 = icmp ne i8 %189, 0
  br i1 %190, label %191, label %198, !prof !31

191:                                              ; preds = %186
  %192 = and i64 %184, 7
  %193 = trunc i64 %192 to i8
  br label %194

194:                                              ; preds = %191
  %195 = icmp sge i8 %193, %189
  br i1 %195, label %196, label %198

196:                                              ; preds = %194
  call void @__asan_report_store1(i64 %184) #8
  br label %197

197:                                              ; preds = %196
  unreachable

198:                                              ; preds = %194, %186
  store i8 %182, i8* %arrayidx20, align 1
  br label %199

199:                                              ; preds = %198
  br label %for.inc

for.inc:                                          ; preds = %199
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([15 x i32]* @__sancov_gen_.10 to i64), i64 24) to i32*)) #8
  %200 = load i32, i32* %i, align 4
  %inc = add nsw i32 %200, 1
  br label %201

201:                                              ; preds = %for.inc
  store i32 %inc, i32* %i, align 4
  br label %for.cond, !llvm.loop !32

for.end:                                          ; preds = %165
  %arrayidx21 = getelementptr inbounds [201 x i8], [201 x i8]* %21, i64 0, i64 16
  %202 = ptrtoint i8* %arrayidx21 to i64
  %203 = lshr i64 %202, 3
  %204 = add i64 %203, 2147450880
  br label %205

205:                                              ; preds = %for.end
  %206 = inttoptr i64 %204 to i8*
  %207 = load i8, i8* %206, align 1
  %208 = icmp ne i8 %207, 0
  br i1 %208, label %209, label %216, !prof !31

209:                                              ; preds = %205
  %210 = and i64 %202, 7
  %211 = trunc i64 %210 to i8
  br label %212

212:                                              ; preds = %209
  %213 = icmp sge i8 %211, %207
  br i1 %213, label %214, label %216

214:                                              ; preds = %212
  call void @__asan_report_store1(i64 %202) #8
  br label %215

215:                                              ; preds = %214
  unreachable

216:                                              ; preds = %212, %205
  store i8 0, i8* %arrayidx21, align 16
  %217 = bitcast i32* %i22 to i8*
  call void @llvm.lifetime.start.p0i8(i64 4, i8* %217) #3
  br label %218

218:                                              ; preds = %216
  store i32 0, i32* %i22, align 4
  br label %for.cond23

for.cond23:                                       ; preds = %258, %218
  %219 = load i32, i32* %i22, align 4
  call void @__sanitizer_cov_trace_const_cmp4(i32 8, i32 %219)
  br label %220

220:                                              ; preds = %for.cond23
  %cmp24 = icmp slt i32 %219, 8
  br i1 %cmp24, label %for.body26, label %for.cond.cleanup25

for.cond.cleanup25:                               ; preds = %220
  store i32 8, i32* %cleanup.dest.slot, align 4
  %221 = bitcast i32* %i22 to i8*
  br label %222

222:                                              ; preds = %for.cond.cleanup25
  call void @llvm.lifetime.end.p0i8(i64 4, i8* %221) #3
  br label %for.end35

for.body26:                                       ; preds = %220
  %223 = load i32, i32* %i22, align 4
  %add27 = add nsw i32 %223, 44
  %add28 = add nsw i32 %add27, 16
  %idxprom29 = sext i32 %add28 to i64
  %arrayidx30 = getelementptr inbounds [201 x i8], [201 x i8]* %17, i64 0, i64 %idxprom29
  %224 = ptrtoint i8* %arrayidx30 to i64
  br label %225

225:                                              ; preds = %for.body26
  %226 = lshr i64 %224, 3
  %227 = add i64 %226, 2147450880
  %228 = inttoptr i64 %227 to i8*
  %229 = load i8, i8* %228, align 1
  %230 = icmp ne i8 %229, 0
  br i1 %230, label %231, label %238, !prof !31

231:                                              ; preds = %225
  %232 = and i64 %224, 7
  %233 = trunc i64 %232 to i8
  br label %234

234:                                              ; preds = %231
  %235 = icmp sge i8 %233, %229
  br i1 %235, label %236, label %238

236:                                              ; preds = %234
  call void @__asan_report_load1(i64 %224) #8
  br label %237

237:                                              ; preds = %236
  unreachable

238:                                              ; preds = %234, %225
  %239 = load i8, i8* %arrayidx30, align 1
  %240 = load i32, i32* %i22, align 4
  %idxprom31 = sext i32 %240 to i64
  %arrayidx32 = getelementptr inbounds [201 x i8], [201 x i8]* %23, i64 0, i64 %idxprom31
  %241 = ptrtoint i8* %arrayidx32 to i64
  %242 = lshr i64 %241, 3
  br label %243

243:                                              ; preds = %238
  %244 = add i64 %242, 2147450880
  %245 = inttoptr i64 %244 to i8*
  %246 = load i8, i8* %245, align 1
  %247 = icmp ne i8 %246, 0
  br i1 %247, label %248, label %255, !prof !31

248:                                              ; preds = %243
  %249 = and i64 %241, 7
  %250 = trunc i64 %249 to i8
  br label %251

251:                                              ; preds = %248
  %252 = icmp sge i8 %250, %246
  br i1 %252, label %253, label %255

253:                                              ; preds = %251
  call void @__asan_report_store1(i64 %241) #8
  br label %254

254:                                              ; preds = %253
  unreachable

255:                                              ; preds = %251, %243
  store i8 %239, i8* %arrayidx32, align 1
  br label %256

256:                                              ; preds = %255
  br label %for.inc33

for.inc33:                                        ; preds = %256
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([15 x i32]* @__sancov_gen_.10 to i64), i64 28) to i32*)) #8
  %257 = load i32, i32* %i22, align 4
  %inc34 = add nsw i32 %257, 1
  br label %258

258:                                              ; preds = %for.inc33
  store i32 %inc34, i32* %i22, align 4
  br label %for.cond23, !llvm.loop !33

for.end35:                                        ; preds = %222
  %arrayidx36 = getelementptr inbounds [201 x i8], [201 x i8]* %23, i64 0, i64 8
  %259 = ptrtoint i8* %arrayidx36 to i64
  %260 = lshr i64 %259, 3
  %261 = add i64 %260, 2147450880
  br label %262

262:                                              ; preds = %for.end35
  %263 = inttoptr i64 %261 to i8*
  %264 = load i8, i8* %263, align 1
  %265 = icmp ne i8 %264, 0
  br i1 %265, label %266, label %273, !prof !31

266:                                              ; preds = %262
  %267 = and i64 %259, 7
  %268 = trunc i64 %267 to i8
  br label %269

269:                                              ; preds = %266
  %270 = icmp sge i8 %268, %264
  br i1 %270, label %271, label %273

271:                                              ; preds = %269
  call void @__asan_report_store1(i64 %259) #8
  br label %272

272:                                              ; preds = %271
  unreachable

273:                                              ; preds = %269, %262
  store i8 0, i8* %arrayidx36, align 8
  %274 = bitcast i32* %i37 to i8*
  call void @llvm.lifetime.start.p0i8(i64 4, i8* %274) #3
  br label %275

275:                                              ; preds = %273
  store i32 0, i32* %i37, align 4
  br label %for.cond38

for.cond38:                                       ; preds = %315, %275
  %276 = load i32, i32* %i37, align 4
  call void @__sanitizer_cov_trace_const_cmp4(i32 4, i32 %276)
  br label %277

277:                                              ; preds = %for.cond38
  %cmp39 = icmp slt i32 %276, 4
  br i1 %cmp39, label %for.body41, label %for.cond.cleanup40

for.cond.cleanup40:                               ; preds = %277
  store i32 11, i32* %cleanup.dest.slot, align 4
  %278 = bitcast i32* %i37 to i8*
  br label %279

279:                                              ; preds = %for.cond.cleanup40
  call void @llvm.lifetime.end.p0i8(i64 4, i8* %278) #3
  br label %for.end51

for.body41:                                       ; preds = %277
  %280 = load i32, i32* %i37, align 4
  %add42 = add nsw i32 %280, 44
  %add43 = add nsw i32 %add42, 16
  %add44 = add nsw i32 %add43, 8
  %idxprom45 = sext i32 %add44 to i64
  %arrayidx46 = getelementptr inbounds [201 x i8], [201 x i8]* %17, i64 0, i64 %idxprom45
  %281 = ptrtoint i8* %arrayidx46 to i64
  br label %282

282:                                              ; preds = %for.body41
  %283 = lshr i64 %281, 3
  %284 = add i64 %283, 2147450880
  %285 = inttoptr i64 %284 to i8*
  %286 = load i8, i8* %285, align 1
  %287 = icmp ne i8 %286, 0
  br i1 %287, label %288, label %295, !prof !31

288:                                              ; preds = %282
  %289 = and i64 %281, 7
  %290 = trunc i64 %289 to i8
  br label %291

291:                                              ; preds = %288
  %292 = icmp sge i8 %290, %286
  br i1 %292, label %293, label %295

293:                                              ; preds = %291
  call void @__asan_report_load1(i64 %281) #8
  br label %294

294:                                              ; preds = %293
  unreachable

295:                                              ; preds = %291, %282
  %296 = load i8, i8* %arrayidx46, align 1
  %297 = load i32, i32* %i37, align 4
  %idxprom47 = sext i32 %297 to i64
  %arrayidx48 = getelementptr inbounds [201 x i8], [201 x i8]* %25, i64 0, i64 %idxprom47
  %298 = ptrtoint i8* %arrayidx48 to i64
  %299 = lshr i64 %298, 3
  br label %300

300:                                              ; preds = %295
  %301 = add i64 %299, 2147450880
  %302 = inttoptr i64 %301 to i8*
  %303 = load i8, i8* %302, align 1
  %304 = icmp ne i8 %303, 0
  br i1 %304, label %305, label %312, !prof !31

305:                                              ; preds = %300
  %306 = and i64 %298, 7
  %307 = trunc i64 %306 to i8
  br label %308

308:                                              ; preds = %305
  %309 = icmp sge i8 %307, %303
  br i1 %309, label %310, label %312

310:                                              ; preds = %308
  call void @__asan_report_store1(i64 %298) #8
  br label %311

311:                                              ; preds = %310
  unreachable

312:                                              ; preds = %308, %300
  store i8 %296, i8* %arrayidx48, align 1
  br label %313

313:                                              ; preds = %312
  br label %for.inc49

for.inc49:                                        ; preds = %313
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([15 x i32]* @__sancov_gen_.10 to i64), i64 32) to i32*)) #8
  %314 = load i32, i32* %i37, align 4
  %inc50 = add nsw i32 %314, 1
  br label %315

315:                                              ; preds = %for.inc49
  store i32 %inc50, i32* %i37, align 4
  br label %for.cond38, !llvm.loop !34

for.end51:                                        ; preds = %279
  %arrayidx52 = getelementptr inbounds [201 x i8], [201 x i8]* %25, i64 0, i64 4
  %316 = ptrtoint i8* %arrayidx52 to i64
  %317 = lshr i64 %316, 3
  %318 = add i64 %317, 2147450880
  br label %319

319:                                              ; preds = %for.end51
  %320 = inttoptr i64 %318 to i8*
  %321 = load i8, i8* %320, align 1
  %322 = icmp ne i8 %321, 0
  br i1 %322, label %323, label %330, !prof !31

323:                                              ; preds = %319
  %324 = and i64 %316, 7
  %325 = trunc i64 %324 to i8
  br label %326

326:                                              ; preds = %323
  %327 = icmp sge i8 %325, %321
  br i1 %327, label %328, label %330

328:                                              ; preds = %326
  call void @__asan_report_store1(i64 %316) #8
  br label %329

329:                                              ; preds = %328
  unreachable

330:                                              ; preds = %326, %319
  store i8 0, i8* %arrayidx52, align 4
  %arraydecay53 = getelementptr inbounds [201 x i8], [201 x i8]* %25, i64 0, i64 0
  %call54 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ({ [4 x i8], [60 x i8] }, { [4 x i8], [60 x i8] }* @.str.8, i32 0, i32 0, i64 0), i8* %arraydecay53)
  %331 = bitcast i64* %x to i8*
  call void @llvm.lifetime.start.p0i8(i64 8, i8* %331) #3
  %arraydecay55 = getelementptr inbounds [201 x i8], [201 x i8]* %21, i64 0, i64 0
  br label %332

332:                                              ; preds = %330
  %call56 = call i64 @strtoull(i8* %arraydecay55, i8** null, i32 16) #3
  store i64 %call56, i64* %x, align 8
  %333 = load i64, i64* %x, align 8
  call void @__sanitizer_cov_trace_const_cmp8(i64 -3819410105351357762, i64 %333)
  %cmp57 = icmp ne i64 %333, -3819410105351357762
  br i1 %cmp57, label %if.then58, label %if.end59

if.then58:                                        ; preds = %332
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([15 x i32]* @__sancov_gen_.10 to i64), i64 36) to i32*)) #8
  store i32 1, i32* %retval, align 4
  br label %334

334:                                              ; preds = %if.then58
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup76

if.end59:                                         ; preds = %332
  %335 = bitcast i32* %y to i8*
  call void @llvm.lifetime.start.p0i8(i64 4, i8* %335) #3
  %arraydecay60 = getelementptr inbounds [201 x i8], [201 x i8]* %23, i64 0, i64 0
  %call61 = call i64 @strtoul(i8* %arraydecay60, i8** null, i32 16) #3
  %conv = trunc i64 %call61 to i32
  br label %336

336:                                              ; preds = %if.end59
  store i32 %conv, i32* %y, align 4
  %337 = load i32, i32* %y, align 4
  call void @__sanitizer_cov_trace_const_cmp4(i32 -559038242, i32 %337)
  %cmp62 = icmp ne i32 %337, -559038242
  br i1 %cmp62, label %if.then63, label %if.end64

if.then63:                                        ; preds = %336
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([15 x i32]* @__sancov_gen_.10 to i64), i64 40) to i32*)) #8
  store i32 1, i32* %retval, align 4
  br label %338

338:                                              ; preds = %if.then63
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup75

if.end64:                                         ; preds = %336
  %339 = bitcast i16* %z to i8*
  call void @llvm.lifetime.start.p0i8(i64 2, i8* %339) #3
  %arraydecay65 = getelementptr inbounds [201 x i8], [201 x i8]* %25, i64 0, i64 0
  %call66 = call i64 @strtouq(i8* %arraydecay65, i8** null, i32 16) #3
  %conv67 = trunc i64 %call66 to i16
  store i16 %conv67, i16* %z, align 2
  br label %340

340:                                              ; preds = %if.end64
  %341 = load i16, i16* %z, align 2
  %conv68 = zext i16 %341 to i32
  %342 = zext i32 %conv68 to i64
  call void @__sanitizer_cov_trace_switch(i64 %342, i64* getelementptr inbounds ([5 x i64], [5 x i64]* @__sancov_gen_cov_switch_values.11, i32 0, i32 0))
  switch i32 %conv68, label %sw.default72 [
    i32 48879, label %sw.bb69
    i32 65259, label %sw.bb70
    i32 61374, label %sw.bb71
  ]

sw.bb69:                                          ; preds = %340
  br label %sw.epilog73

sw.bb70:                                          ; preds = %340
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([15 x i32]* @__sancov_gen_.10 to i64), i64 44) to i32*)) #8
  store i32 1, i32* %retval, align 4
  br label %343

343:                                              ; preds = %sw.bb70
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup

sw.bb71:                                          ; preds = %340
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([15 x i32]* @__sancov_gen_.10 to i64), i64 48) to i32*)) #8
  store i32 1, i32* %retval, align 4
  br label %344

344:                                              ; preds = %sw.bb71
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup

sw.default72:                                     ; preds = %340
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([15 x i32]* @__sancov_gen_.10 to i64), i64 52) to i32*)) #8
  store i32 1, i32* %retval, align 4
  br label %345

345:                                              ; preds = %sw.default72
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup

sw.epilog73:                                      ; preds = %sw.bb69
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([15 x i32]* @__sancov_gen_.10 to i64), i64 56) to i32*)) #8
  %call74 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ({ [33 x i8], [63 x i8] }, { [33 x i8], [63 x i8] }* @.str.9, i32 0, i32 0, i64 0))
  store i32 0, i32* %retval, align 4
  br label %346

346:                                              ; preds = %sw.epilog73
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup

cleanup:                                          ; preds = %346, %345, %344, %343
  %347 = bitcast i16* %z to i8*
  call void @llvm.lifetime.end.p0i8(i64 2, i8* %347) #3
  br label %348

348:                                              ; preds = %cleanup
  br label %cleanup75

cleanup75:                                        ; preds = %348, %338
  %349 = bitcast i32* %y to i8*
  call void @llvm.lifetime.end.p0i8(i64 4, i8* %349) #3
  br label %350

350:                                              ; preds = %cleanup75
  br label %cleanup76

cleanup76:                                        ; preds = %350, %334
  %351 = bitcast i64* %x to i8*
  call void @llvm.lifetime.end.p0i8(i64 8, i8* %351) #3
  %352 = bitcast [201 x i8]* %25 to i8*
  %353 = add i64 %32, 118
  %354 = inttoptr i64 %353 to i64*
  store i64 -506381209866536712, i64* %354, align 1
  %355 = add i64 %32, 126
  %356 = inttoptr i64 %355 to i64*
  store i64 -506381209866536712, i64* %356, align 1
  %357 = add i64 %32, 134
  %358 = inttoptr i64 %357 to i64*
  store i64 -506381209866536712, i64* %358, align 1
  %359 = add i64 %32, 142
  %360 = inttoptr i64 %359 to i16*
  store i16 -1800, i16* %360, align 1
  call void @llvm.lifetime.end.p0i8(i64 201, i8* %352) #3
  %361 = bitcast [201 x i8]* %23 to i8*
  %362 = add i64 %32, 84
  %363 = inttoptr i64 %362 to i64*
  store i64 -506381209866536712, i64* %363, align 1
  %364 = add i64 %32, 92
  %365 = inttoptr i64 %364 to i64*
  store i64 -506381209866536712, i64* %365, align 1
  br label %366

366:                                              ; preds = %cleanup76
  %367 = add i64 %32, 100
  %368 = inttoptr i64 %367 to i64*
  store i64 -506381209866536712, i64* %368, align 1
  %369 = add i64 %32, 108
  %370 = inttoptr i64 %369 to i16*
  store i16 -1800, i16* %370, align 1
  call void @llvm.lifetime.end.p0i8(i64 201, i8* %361) #3
  %371 = bitcast [201 x i8]* %21 to i8*
  %372 = add i64 %32, 50
  %373 = inttoptr i64 %372 to i64*
  store i64 -506381209866536712, i64* %373, align 1
  %374 = add i64 %32, 58
  %375 = inttoptr i64 %374 to i64*
  store i64 -506381209866536712, i64* %375, align 1
  %376 = add i64 %32, 66
  %377 = inttoptr i64 %376 to i64*
  store i64 -506381209866536712, i64* %377, align 1
  %378 = add i64 %32, 74
  %379 = inttoptr i64 %378 to i16*
  store i16 -1800, i16* %379, align 1
  call void @llvm.lifetime.end.p0i8(i64 201, i8* %371) #3
  br label %cleanup80

cleanup80:                                        ; preds = %366, %132
  %380 = bitcast [45 x i8]* %19 to i8*
  %381 = add i64 %32, 40
  %382 = inttoptr i64 %381 to i32*
  store i32 -117901064, i32* %382, align 1
  %383 = add i64 %32, 44
  %384 = inttoptr i64 %383 to i16*
  store i16 -1800, i16* %384, align 1
  call void @llvm.lifetime.end.p0i8(i64 45, i8* %380) #3
  %385 = bitcast %struct._IO_FILE** %fp to i8*
  call void @llvm.lifetime.end.p0i8(i64 8, i8* %385) #3
  %386 = bitcast [201 x i8]* %17 to i8*
  %387 = add i64 %32, 6
  %388 = inttoptr i64 %387 to i64*
  store i64 -506381209866536712, i64* %388, align 1
  %389 = add i64 %32, 14
  %390 = inttoptr i64 %389 to i64*
  store i64 -506381209866536712, i64* %390, align 1
  %391 = add i64 %32, 22
  %392 = inttoptr i64 %391 to i64*
  br label %393

393:                                              ; preds = %cleanup80
  store i64 -506381209866536712, i64* %392, align 1
  %394 = add i64 %32, 30
  %395 = inttoptr i64 %394 to i16*
  store i16 -1800, i16* %395, align 1
  call void @llvm.lifetime.end.p0i8(i64 201, i8* %386) #3
  %396 = bitcast i8** %filename to i8*
  call void @llvm.lifetime.end.p0i8(i64 8, i8* %396) #3
  %397 = bitcast i32* %15 to i8*
  %398 = add i64 %32, 4
  %399 = inttoptr i64 %398 to i8*
  store i8 -8, i8* %399, align 1
  call void @llvm.lifetime.end.p0i8(i64 4, i8* %397) #3
  %400 = bitcast i32* %opt to i8*
  call void @llvm.lifetime.end.p0i8(i64 4, i8* %400) #3
  %401 = load i32, i32* %retval, align 4
  store i64 1172321806, i64* %26, align 8
  %402 = icmp ne i64 %7, 0
  br i1 %402, label %403, label %405

403:                                              ; preds = %393
  call void @__asan_stack_free_5(i64 %7, i64 1216)
  br label %404

404:                                              ; preds = %403
  br label %408

405:                                              ; preds = %393
  %406 = add i64 %32, 0
  call void @__asan_set_shadow_00(i64 %406, i64 152)
  br label %407

407:                                              ; preds = %405
  br label %408

408:                                              ; preds = %407, %404
  ret i32 %401
}

; Function Attrs: argmemonly nofree nosync nounwind willreturn
declare void @llvm.lifetime.start.p0i8(i64 immarg, i8* nocapture) #5

; Function Attrs: nounwind
declare dso_local i32 @getopt_long(i32, i8**, i8*, %struct.option*, i32*) #2

declare dso_local i32 @printf(i8*, ...) #1

declare dso_local %struct._IO_FILE* @fopen(i8*, i8*) #1

declare dso_local i8* @fgets(i8*, i32, %struct._IO_FILE*) #1

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

; Function Attrs: argmemonly nofree nosync nounwind willreturn
declare void @llvm.lifetime.end.p0i8(i64 immarg, i8* nocapture) #5

; Function Attrs: nounwind
declare dso_local i64 @strtoull(i8*, i8**, i32) #2

; Function Attrs: nounwind
declare dso_local i64 @strtoul(i8*, i8**, i32) #2

; Function Attrs: nounwind
declare dso_local i64 @strtouq(i8*, i8**, i32) #2

; Function Attrs: noinline sanitize_address uwtable
define internal void @_GLOBAL__sub_I_demo.cc() #0 section ".text.startup" comdat($"_GLOBAL__sub_I_demo.cc$21576b91ab9b15712202e1b4a494877f") {
entry:
  call void @__asan_before_dynamic_init(i64 ptrtoint ([13 x i8]* @___asan_gen_.13 to i64))
  call void @__sanitizer_cov_trace_pc_guard(i32* getelementptr inbounds ([1 x i32], [1 x i32]* @__sancov_gen_.12, i32 0, i32 0)) #8
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
  call void @__asan_before_dynamic_init(i64 ptrtoint ([13 x i8]* @___asan_gen_.13 to i64))
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
  call void @__asan_register_globals(i64 ptrtoint ([12 x { i64, i64, i64, i64, i64, i64, i64, i64 }]* @0 to i64), i64 12)
  ret void
}

declare void @__asan_version_mismatch_check_v8()

define internal void @asan.module_dtor() {
  call void @__asan_unregister_globals(i64 ptrtoint ([12 x { i64, i64, i64, i64, i64, i64, i64, i64 }]* @0 to i64), i64 12)
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

!llvm.asan.globals = !{!3, !5, !7, !9, !11, !13, !15, !17, !19, !21, !23, !25}
!llvm.module.flags = !{!27}
!llvm.ident = !{!28}

!0 = !{void ()* @__cxx_global_var_init}
!1 = !{i32 (i32, i8**)* @main}
!2 = !{void ()* @_GLOBAL__sub_I_demo.cc}
!3 = !{%"class.std::ios_base::Init"* getelementptr inbounds ({ %"class.std::ios_base::Init", [63 x i8] }, { %"class.std::ios_base::Init", [63 x i8] }* @_ZStL8__ioinit, i32 0, i32 0), !4, !"std::__ioinit", i1 true, i1 false}
!4 = !{!"/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/iostream", i32 74, i32 25}
!5 = !{[5 x i8]* getelementptr inbounds ({ [5 x i8], [59 x i8] }, { [5 x i8], [59 x i8] }* @.str, i32 0, i32 0), !6, !"<string literal>", i1 false, i1 false}
!6 = !{!"demo/demo.cc", i32 20, i32 10}
!7 = !{[1 x %struct.option]* getelementptr inbounds ({ [1 x %struct.option], [32 x i8] }, { [1 x %struct.option], [32 x i8] }* @_ZZ4mainE12long_options, i32 0, i32 0), !8, !"long_options", i1 false, i1 false}
!8 = !{!"demo/demo.cc", i32 18, i32 26}
!9 = !{[3 x i8]* getelementptr inbounds ({ [3 x i8], [61 x i8] }, { [3 x i8], [61 x i8] }* @.str.1, i32 0, i32 0), !10, !"<string literal>", i1 false, i1 false}
!10 = !{!"demo/demo.cc", i32 22, i32 42}
!11 = !{[18 x i8]* getelementptr inbounds ({ [18 x i8], [46 x i8] }, { [18 x i8], [46 x i8] }* @.str.2, i32 0, i32 0), !12, !"<string literal>", i1 false, i1 false}
!12 = !{!"demo/demo.cc", i32 31, i32 20}
!13 = !{[2 x i8]* getelementptr inbounds ({ [2 x i8], [62 x i8] }, { [2 x i8], [62 x i8] }* @.str.3, i32 0, i32 0), !14, !"<string literal>", i1 false, i1 false}
!14 = !{!"demo/demo.cc", i32 39, i32 32}
!15 = !{[21 x i8]* getelementptr inbounds ({ [21 x i8], [43 x i8] }, { [21 x i8], [43 x i8] }* @.str.4, i32 0, i32 0), !16, !"<string literal>", i1 false, i1 false}
!16 = !{!"demo/demo.cc", i32 52, i32 28}
!17 = !{[12 x i8]* getelementptr inbounds ({ [12 x i8], [52 x i8] }, { [12 x i8], [52 x i8] }* @.str.5, i32 0, i32 0), !18, !"<string literal>", i1 false, i1 false}
!18 = !{!"demo/demo.cc", i32 53, i32 30}
!19 = !{[14 x i8]* getelementptr inbounds ({ [14 x i8], [50 x i8] }, { [14 x i8], [50 x i8] }* @.str.6, i32 0, i32 0), !20, !"<string literal>", i1 false, i1 false}
!20 = !{!"demo/demo.cc", i32 54, i32 29}
!21 = !{[27 x i8]* getelementptr inbounds ({ [27 x i8], [37 x i8] }, { [27 x i8], [37 x i8] }* @.str.7, i32 0, i32 0), !22, !"<string literal>", i1 false, i1 false}
!22 = !{!"demo/demo.cc", i32 58, i32 12}
!23 = !{[4 x i8]* getelementptr inbounds ({ [4 x i8], [60 x i8] }, { [4 x i8], [60 x i8] }* @.str.8, i32 0, i32 0), !24, !"<string literal>", i1 false, i1 false}
!24 = !{!"demo/demo.cc", i32 73, i32 12}
!25 = !{[33 x i8]* getelementptr inbounds ({ [33 x i8], [63 x i8] }, { [33 x i8], [63 x i8] }* @.str.9, i32 0, i32 0), !26, !"<string literal>", i1 false, i1 false}
!26 = !{!"demo/demo.cc", i32 101, i32 12}
!27 = !{i32 1, !"wchar_size", i32 4}
!28 = !{!"clang version 12.0.1 (git@github.com:fengzhengzhan/BTFuzz.git 0b64f5806b4302732328fa068687800669443ef8)"}
!29 = distinct !{!29, !30}
!30 = !{!"llvm.loop.mustprogress"}
!31 = !{!"branch_weights", i32 1, i32 100000}
!32 = distinct !{!32, !30}
!33 = distinct !{!33, !30}
!34 = distinct !{!34, !30}
