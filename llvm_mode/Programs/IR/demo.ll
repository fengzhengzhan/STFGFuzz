; ModuleID = 'demo/demo.cc'
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
@.str.4 = internal constant { [27 x i8], [37 x i8] } { [27 x i8] c"---------------------   %c\00", [37 x i8] zeroinitializer }, align 32
@.str.5 = internal constant { [21 x i8], [43 x i8] } { [21 x i8] c"The quick brown fox \00", [43 x i8] zeroinitializer }, align 32
@.str.6 = internal constant { [12 x i8], [52 x i8] } { [12 x i8] c"jumps over \00", [52 x i8] zeroinitializer }, align 32
@.str.7 = internal constant { [14 x i8], [50 x i8] } { [14 x i8] c"the lazy dog.\00", [50 x i8] zeroinitializer }, align 32
@.str.8 = internal constant { [27 x i8], [37 x i8] } { [27 x i8] c"Though first str/mem Cmp.\0A\00", [37 x i8] zeroinitializer }, align 32
@.str.9 = internal constant { [4 x i8], [60 x i8] } { [4 x i8] c"%s\0A\00", [60 x i8] zeroinitializer }, align 32
@.str.10 = internal constant { [33 x i8], [63 x i8] } { [33 x i8] c"Puzzle solved, Congratulations!\0A\00", [63 x i8] zeroinitializer }, align 32
@__sancov_lowest_stack = external thread_local(initialexec) global i64
@__sancov_gen_ = private global [1 x i32] zeroinitializer, section "__sancov_guards", comdat($"__cxx_global_var_init$21576b91ab9b15712202e1b4a494877f"), align 4, !associated !0
@__sancov_gen_.11 = private global [13 x i32] zeroinitializer, section "__sancov_guards", comdat($main), align 4, !associated !1
@__sancov_gen_cov_switch_values = internal global [3 x i64] [i64 1, i64 32, i64 102]
@__sancov_gen_cov_switch_values.12 = internal global [3 x i64] [i64 1, i64 32, i64 48879]
@__sancov_gen_.13 = private global [1 x i32] zeroinitializer, section "__sancov_guards", comdat($"_GLOBAL__sub_I_demo.cc$21576b91ab9b15712202e1b4a494877f"), align 4, !associated !2
@__start___sancov_guards = external hidden global i32
@__stop___sancov_guards = external hidden global i32
@__asan_option_detect_stack_use_after_return = external global i32
@___asan_gen_ = private unnamed_addr constant [87 x i8] c"6 32 4 9 opt_index 48 201 3 str 320 45 6 buffer 400 201 2 s1 672 201 2 s2 944 201 2 s3\00", align 1
@___asan_gen_.14 = private constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.15 = private unnamed_addr constant [14 x i8] c"std::__ioinit\00", align 1
@___asan_gen_.16 = private unnamed_addr constant [67 x i8] c"/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/iostream\00", align 1
@___asan_gen_.17 = private unnamed_addr constant { [67 x i8]*, i32, i32 } { [67 x i8]* @___asan_gen_.16, i32 74, i32 25 }
@___asan_gen_.18 = private unnamed_addr constant [13 x i8] c"long_options\00", align 1
@___asan_gen_.19 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.20 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.19, i32 18, i32 26 }
@___asan_gen_.21 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.22 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.23 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.22, i32 20, i32 10 }
@___asan_gen_.24 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.25 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.26 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.25, i32 22, i32 42 }
@___asan_gen_.27 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.28 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.29 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.28, i32 31, i32 20 }
@___asan_gen_.30 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.31 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.32 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.31, i32 39, i32 32 }
@___asan_gen_.33 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.34 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.35 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.34, i32 46, i32 12 }
@___asan_gen_.36 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.37 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.38 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.37, i32 52, i32 28 }
@___asan_gen_.39 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.40 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.41 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.40, i32 53, i32 30 }
@___asan_gen_.42 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.43 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.44 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.43, i32 54, i32 29 }
@___asan_gen_.45 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.46 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.47 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.46, i32 58, i32 12 }
@___asan_gen_.48 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.49 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.50 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.49, i32 73, i32 12 }
@___asan_gen_.51 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.52 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.53 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.52, i32 95, i32 12 }
@llvm.compiler.used = appending global [16 x i8*] [i8* bitcast ([1 x i32]* @__sancov_gen_ to i8*), i8* bitcast ([13 x i32]* @__sancov_gen_.11 to i8*), i8* bitcast ([1 x i32]* @__sancov_gen_.13 to i8*), i8* getelementptr inbounds ({ %"class.std::ios_base::Init", [63 x i8] }, { %"class.std::ios_base::Init", [63 x i8] }* @_ZStL8__ioinit, i32 0, i32 0, i32 0), i8* bitcast ({ [1 x %struct.option], [32 x i8] }* @_ZZ4mainE12long_options to i8*), i8* getelementptr inbounds ({ [5 x i8], [59 x i8] }, { [5 x i8], [59 x i8] }* @.str, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [3 x i8], [61 x i8] }, { [3 x i8], [61 x i8] }* @.str.1, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [18 x i8], [46 x i8] }, { [18 x i8], [46 x i8] }* @.str.2, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [2 x i8], [62 x i8] }, { [2 x i8], [62 x i8] }* @.str.3, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [27 x i8], [37 x i8] }, { [27 x i8], [37 x i8] }* @.str.4, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [21 x i8], [43 x i8] }, { [21 x i8], [43 x i8] }* @.str.5, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [12 x i8], [52 x i8] }, { [12 x i8], [52 x i8] }* @.str.6, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [14 x i8], [50 x i8] }, { [14 x i8], [50 x i8] }* @.str.7, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [27 x i8], [37 x i8] }, { [27 x i8], [37 x i8] }* @.str.8, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [4 x i8], [60 x i8] }, { [4 x i8], [60 x i8] }* @.str.9, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [33 x i8], [63 x i8] }, { [33 x i8], [63 x i8] }* @.str.10, i32 0, i32 0, i32 0)], section "llvm.metadata"
@0 = internal global [13 x { i64, i64, i64, i64, i64, i64, i64, i64 }] [{ i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ %"class.std::ios_base::Init", [63 x i8] }* @_ZStL8__ioinit to i64), i64 1, i64 64, i64 ptrtoint ([14 x i8]* @___asan_gen_.15 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64), i64 1, i64 ptrtoint ({ [67 x i8]*, i32, i32 }* @___asan_gen_.17 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [1 x %struct.option], [32 x i8] }* @_ZZ4mainE12long_options to i64), i64 32, i64 64, i64 ptrtoint ([13 x i8]* @___asan_gen_.18 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.20 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [5 x i8], [59 x i8] }* @.str to i64), i64 5, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.21 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.23 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [3 x i8], [61 x i8] }* @.str.1 to i64), i64 3, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.24 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.26 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [18 x i8], [46 x i8] }* @.str.2 to i64), i64 18, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.27 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.29 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [2 x i8], [62 x i8] }* @.str.3 to i64), i64 2, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.30 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.32 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [27 x i8], [37 x i8] }* @.str.4 to i64), i64 27, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.33 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.35 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [21 x i8], [43 x i8] }* @.str.5 to i64), i64 21, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.36 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.38 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [12 x i8], [52 x i8] }* @.str.6 to i64), i64 12, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.39 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.41 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [14 x i8], [50 x i8] }* @.str.7 to i64), i64 14, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.42 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.44 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [27 x i8], [37 x i8] }* @.str.8 to i64), i64 27, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.45 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.47 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [4 x i8], [60 x i8] }* @.str.9 to i64), i64 4, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.48 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.50 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [33 x i8], [63 x i8] }* @.str.10 to i64), i64 33, i64 96, i64 ptrtoint ([17 x i8]* @___asan_gen_.51 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.53 to i64), i64 -1 }]
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
  %opt = alloca i32, align 4
  %filename = alloca i8*, align 8
  %fp = alloca %struct._IO_FILE*, align 8
  %cleanup.dest.slot = alloca i32, align 4
  %i = alloca i32, align 4
  %i24 = alloca i32, align 4
  %i39 = alloca i32, align 4
  %x = alloca i64, align 8
  %y = alloca i32, align 4
  %z = alloca i16, align 2
  %asan_local_stack_base = alloca i64, align 8
  %0 = load i32, i32* @__asan_option_detect_stack_use_after_return, align 4
  %1 = icmp ne i32 %0, 0
  br i1 %1, label %2, label %4

2:                                                ; preds = %entry
  %3 = call i64 @__asan_stack_malloc_5(i64 1216)
  br label %4

4:                                                ; preds = %entry, %2
  %5 = phi i64 [ 0, %entry ], [ %3, %2 ]
  %6 = icmp eq i64 %5, 0
  br i1 %6, label %7, label %9

7:                                                ; preds = %4
  %MyAlloca = alloca i8, i64 1216, align 32
  %8 = ptrtoint i8* %MyAlloca to i64
  br label %9

9:                                                ; preds = %4, %7
  %10 = phi i64 [ %5, %4 ], [ %8, %7 ]
  store i64 %10, i64* %asan_local_stack_base, align 8
  %11 = add i64 %10, 32
  %12 = inttoptr i64 %11 to i32*
  %13 = add i64 %10, 48
  %14 = inttoptr i64 %13 to [201 x i8]*
  %15 = add i64 %10, 320
  %16 = inttoptr i64 %15 to [45 x i8]*
  %17 = add i64 %10, 400
  %18 = inttoptr i64 %17 to [201 x i8]*
  %19 = add i64 %10, 672
  %20 = inttoptr i64 %19 to [201 x i8]*
  %21 = add i64 %10, 944
  %22 = inttoptr i64 %21 to [201 x i8]*
  %23 = inttoptr i64 %10 to i64*
  store i64 1102416563, i64* %23, align 8
  %24 = add i64 %10, 8
  %25 = inttoptr i64 %24 to i64*
  store i64 ptrtoint ([87 x i8]* @___asan_gen_ to i64), i64* %25, align 8
  %26 = add i64 %10, 16
  %27 = inttoptr i64 %26 to i64*
  store i64 ptrtoint (i32 (i32, i8**)* @main to i64), i64* %27, align 8
  %28 = lshr i64 %10, 3
  %29 = add i64 %28, 2147450880
  %30 = add i64 %29, 0
  %31 = inttoptr i64 %30 to i64*
  store i64 -506387807054204431, i64* %31, align 1
  %32 = add i64 %29, 8
  %33 = inttoptr i64 %32 to i64*
  store i64 -506381209866536712, i64* %33, align 1
  %34 = add i64 %29, 16
  %35 = inttoptr i64 %34 to i64*
  store i64 -506381209866536712, i64* %35, align 1
  %36 = add i64 %29, 24
  %37 = inttoptr i64 %36 to i64*
  store i64 -506381209866536712, i64* %37, align 1
  %38 = add i64 %29, 32
  %39 = inttoptr i64 %38 to i64*
  store i64 -940422246894996750, i64* %39, align 1
  %40 = add i64 %29, 40
  %41 = inttoptr i64 %40 to i64*
  store i64 -940415623954368264, i64* %41, align 1
  %42 = add i64 %29, 48
  %43 = inttoptr i64 %42 to i64*
  store i64 -506381209866538254, i64* %43, align 1
  %44 = add i64 %29, 56
  %45 = inttoptr i64 %44 to i64*
  store i64 -506381209866536712, i64* %45, align 1
  %46 = add i64 %29, 64
  %47 = inttoptr i64 %46 to i64*
  store i64 -506381209866536712, i64* %47, align 1
  %48 = add i64 %29, 72
  %49 = inttoptr i64 %48 to i64*
  store i64 -940422246793938696, i64* %49, align 1
  %50 = add i64 %29, 80
  %51 = inttoptr i64 %50 to i64*
  store i64 -506381209967594766, i64* %51, align 1
  %52 = add i64 %29, 88
  %53 = inttoptr i64 %52 to i64*
  store i64 -506381209866536712, i64* %53, align 1
  %54 = add i64 %29, 96
  %55 = inttoptr i64 %54 to i64*
  store i64 -506381209866536712, i64* %55, align 1
  %56 = add i64 %29, 104
  %57 = inttoptr i64 %56 to i64*
  store i64 -940415623954368264, i64* %57, align 1
  %58 = add i64 %29, 112
  %59 = inttoptr i64 %58 to i64*
  store i64 -506387832807165198, i64* %59, align 1
  %60 = add i64 %29, 120
  %61 = inttoptr i64 %60 to i64*
  store i64 -506381209866536712, i64* %61, align 1
  %62 = add i64 %29, 128
  %63 = inttoptr i64 %62 to i64*
  store i64 -506381209866536712, i64* %63, align 1
  %64 = add i64 %29, 136
  %65 = inttoptr i64 %64 to i64*
  store i64 -506381209866536712, i64* %65, align 1
  %66 = add i64 %29, 144
  %67 = inttoptr i64 %66 to i64*
  store i64 -868082074056920077, i64* %67, align 1
  call void @__sanitizer_cov_trace_pc_guard(i32* getelementptr inbounds ([13 x i32], [13 x i32]* @__sancov_gen_.11, i32 0, i32 0)) #8
  store i32 0, i32* %retval, align 4
  store i32 %argc, i32* %argc.addr, align 4
  store i8** %argv, i8*** %argv.addr, align 8
  %68 = bitcast i32* %opt to i8*
  call void @llvm.lifetime.start.p0i8(i64 4, i8* %68) #3
  %69 = bitcast i32* %12 to i8*
  %70 = add i64 %29, 4
  %71 = inttoptr i64 %70 to i8*
  store i8 4, i8* %71, align 1
  call void @llvm.lifetime.start.p0i8(i64 4, i8* %69) #3
  %72 = bitcast i8** %filename to i8*
  call void @llvm.lifetime.start.p0i8(i64 8, i8* %72) #3
  br label %while.cond

while.cond:                                       ; preds = %sw.epilog, %9
  %73 = load i32, i32* %argc.addr, align 4
  %74 = load i8**, i8*** %argv.addr, align 8
  %call = call i32 @getopt_long(i32 %73, i8** %74, i8* getelementptr inbounds ({ [3 x i8], [61 x i8] }, { [3 x i8], [61 x i8] }* @.str.1, i32 0, i32 0, i64 0), %struct.option* getelementptr inbounds ({ [1 x %struct.option], [32 x i8] }, { [1 x %struct.option], [32 x i8] }* @_ZZ4mainE12long_options, i32 0, i32 0, i64 0), i32* %12) #3
  store i32 %call, i32* %opt, align 4
  call void @__sanitizer_cov_trace_const_cmp4(i32 -1, i32 %call)
  %cmp = icmp ne i32 %call, -1
  br i1 %cmp, label %while.body, label %while.end

while.body:                                       ; preds = %while.cond
  %75 = load i32, i32* %opt, align 4
  %76 = zext i32 %75 to i64
  call void @__sanitizer_cov_trace_switch(i64 %76, i64* getelementptr inbounds ([3 x i64], [3 x i64]* @__sancov_gen_cov_switch_values, i32 0, i32 0))
  switch i32 %75, label %sw.default [
    i32 102, label %sw.bb
  ]

sw.bb:                                            ; preds = %while.body
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([13 x i32]* @__sancov_gen_.11 to i64), i64 4) to i32*)) #8
  %77 = load i8, i8* inttoptr (i64 add (i64 lshr (i64 ptrtoint (i8** @optarg to i64), i64 3), i64 2147450880) to i8*), align 1
  %78 = icmp ne i8 %77, 0
  br i1 %78, label %79, label %80

79:                                               ; preds = %sw.bb
  call void @__asan_report_load8(i64 ptrtoint (i8** @optarg to i64)) #8
  unreachable

80:                                               ; preds = %sw.bb
  %81 = load i8*, i8** @optarg, align 8
  store i8* %81, i8** %filename, align 8
  br label %sw.epilog

sw.default:                                       ; preds = %while.body
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([13 x i32]* @__sancov_gen_.11 to i64), i64 8) to i32*)) #8
  %call1 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ({ [18 x i8], [46 x i8] }, { [18 x i8], [46 x i8] }* @.str.2, i32 0, i32 0, i64 0))
  br label %sw.epilog

sw.epilog:                                        ; preds = %sw.default, %80
  br label %while.cond, !llvm.loop !31

while.end:                                        ; preds = %while.cond
  %82 = bitcast [201 x i8]* %14 to i8*
  %83 = add i64 %29, 6
  %84 = inttoptr i64 %83 to i64*
  store i64 0, i64* %84, align 1
  %85 = add i64 %29, 14
  %86 = inttoptr i64 %85 to i64*
  store i64 0, i64* %86, align 1
  %87 = add i64 %29, 22
  %88 = inttoptr i64 %87 to i64*
  store i64 0, i64* %88, align 1
  %89 = add i64 %29, 30
  %90 = inttoptr i64 %89 to i16*
  store i16 256, i16* %90, align 1
  call void @llvm.lifetime.start.p0i8(i64 201, i8* %82) #3
  %91 = bitcast %struct._IO_FILE** %fp to i8*
  call void @llvm.lifetime.start.p0i8(i64 8, i8* %91) #3
  %92 = load i8*, i8** %filename, align 8
  %call2 = call %struct._IO_FILE* @fopen(i8* %92, i8* getelementptr inbounds ({ [2 x i8], [62 x i8] }, { [2 x i8], [62 x i8] }* @.str.3, i32 0, i32 0, i64 0))
  store %struct._IO_FILE* %call2, %struct._IO_FILE** %fp, align 8
  %arraydecay = getelementptr inbounds [201 x i8], [201 x i8]* %14, i64 0, i64 0
  %93 = load %struct._IO_FILE*, %struct._IO_FILE** %fp, align 8
  %call3 = call i8* @fgets(i8* %arraydecay, i32 201, %struct._IO_FILE* %93)
  %94 = bitcast [45 x i8]* %16 to i8*
  %95 = add i64 %29, 40
  %96 = inttoptr i64 %95 to i32*
  store i32 0, i32* %96, align 1
  %97 = add i64 %29, 44
  %98 = inttoptr i64 %97 to i16*
  store i16 1280, i16* %98, align 1
  call void @llvm.lifetime.start.p0i8(i64 45, i8* %94) #3
  %99 = bitcast [45 x i8]* %16 to i8*
  %100 = call i8* @__asan_memset(i8* %99, i32 0, i64 45)
  %arraydecay4 = getelementptr inbounds [45 x i8], [45 x i8]* %16, i64 0, i64 0
  %arraydecay5 = getelementptr inbounds [201 x i8], [201 x i8]* %14, i64 0, i64 0
  %101 = call i8* @__asan_memcpy(i8* %arraydecay4, i8* %arraydecay5, i64 44)
  %arrayidx = getelementptr inbounds [45 x i8], [45 x i8]* %16, i64 0, i64 44
  %102 = ptrtoint i8* %arrayidx to i64
  %103 = lshr i64 %102, 3
  %104 = add i64 %103, 2147450880
  %105 = inttoptr i64 %104 to i8*
  %106 = load i8, i8* %105, align 1
  %107 = icmp ne i8 %106, 0
  br i1 %107, label %108, label %113, !prof !33

108:                                              ; preds = %while.end
  %109 = and i64 %102, 7
  %110 = trunc i64 %109 to i8
  %111 = icmp sge i8 %110, %106
  br i1 %111, label %112, label %113

112:                                              ; preds = %108
  call void @__asan_report_load1(i64 %102) #8
  unreachable

113:                                              ; preds = %108, %while.end
  %114 = load i8, i8* %arrayidx, align 4
  %conv = sext i8 %114 to i32
  %call6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ({ [27 x i8], [37 x i8] }, { [27 x i8], [37 x i8] }* @.str.4, i32 0, i32 0, i64 0), i32 %conv)
  %arrayidx7 = getelementptr inbounds [45 x i8], [45 x i8]* %16, i64 0, i64 44
  %115 = ptrtoint i8* %arrayidx7 to i64
  %116 = lshr i64 %115, 3
  %117 = add i64 %116, 2147450880
  %118 = inttoptr i64 %117 to i8*
  %119 = load i8, i8* %118, align 1
  %120 = icmp ne i8 %119, 0
  br i1 %120, label %121, label %126, !prof !33

121:                                              ; preds = %113
  %122 = and i64 %115, 7
  %123 = trunc i64 %122 to i8
  %124 = icmp sge i8 %123, %119
  br i1 %124, label %125, label %126

125:                                              ; preds = %121
  call void @__asan_report_store1(i64 %115) #8
  unreachable

126:                                              ; preds = %121, %113
  store i8 0, i8* %arrayidx7, align 4
  %arrayidx8 = getelementptr inbounds [45 x i8], [45 x i8]* %16, i64 0, i64 0
  %call9 = call i32 @memcmp(i8* %arrayidx8, i8* getelementptr inbounds ({ [21 x i8], [43 x i8] }, { [21 x i8], [43 x i8] }* @.str.5, i32 0, i32 0, i64 0), i64 20) #9
  call void @__sanitizer_cov_trace_const_cmp4(i32 0, i32 %call9)
  %cmp10 = icmp ne i32 %call9, 0
  br i1 %cmp10, label %while.end.if.then_crit_edge, label %lor.lhs.false

while.end.if.then_crit_edge:                      ; preds = %126
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([13 x i32]* @__sancov_gen_.11 to i64), i64 12) to i32*)) #8
  br label %if.then

lor.lhs.false:                                    ; preds = %126
  %arrayidx11 = getelementptr inbounds [45 x i8], [45 x i8]* %16, i64 0, i64 20
  %call12 = call i32 @strncmp(i8* %arrayidx11, i8* getelementptr inbounds ({ [12 x i8], [52 x i8] }, { [12 x i8], [52 x i8] }* @.str.6, i32 0, i32 0, i64 0), i64 11) #10
  call void @__sanitizer_cov_trace_const_cmp4(i32 0, i32 %call12)
  %cmp13 = icmp ne i32 %call12, 0
  br i1 %cmp13, label %lor.lhs.false.if.then_crit_edge, label %lor.lhs.false14

lor.lhs.false.if.then_crit_edge:                  ; preds = %lor.lhs.false
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([13 x i32]* @__sancov_gen_.11 to i64), i64 16) to i32*)) #8
  br label %if.then

lor.lhs.false14:                                  ; preds = %lor.lhs.false
  %arrayidx15 = getelementptr inbounds [45 x i8], [45 x i8]* %16, i64 0, i64 31
  %call16 = call i32 @strcmp(i8* %arrayidx15, i8* getelementptr inbounds ({ [14 x i8], [50 x i8] }, { [14 x i8], [50 x i8] }* @.str.7, i32 0, i32 0, i64 0)) #9
  call void @__sanitizer_cov_trace_const_cmp4(i32 0, i32 %call16)
  %cmp17 = icmp ne i32 %call16, 0
  br i1 %cmp17, label %lor.lhs.false14.if.then_crit_edge, label %if.end

lor.lhs.false14.if.then_crit_edge:                ; preds = %lor.lhs.false14
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([13 x i32]* @__sancov_gen_.11 to i64), i64 20) to i32*)) #8
  br label %if.then

if.then:                                          ; preds = %lor.lhs.false14.if.then_crit_edge, %lor.lhs.false.if.then_crit_edge, %while.end.if.then_crit_edge
  store i32 1, i32* %retval, align 4
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup81

if.end:                                           ; preds = %lor.lhs.false14
  %call18 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ({ [27 x i8], [37 x i8] }, { [27 x i8], [37 x i8] }* @.str.8, i32 0, i32 0, i64 0))
  %127 = bitcast [201 x i8]* %18 to i8*
  %128 = add i64 %29, 50
  %129 = inttoptr i64 %128 to i64*
  store i64 0, i64* %129, align 1
  %130 = add i64 %29, 58
  %131 = inttoptr i64 %130 to i64*
  store i64 0, i64* %131, align 1
  %132 = add i64 %29, 66
  %133 = inttoptr i64 %132 to i64*
  store i64 0, i64* %133, align 1
  %134 = add i64 %29, 74
  %135 = inttoptr i64 %134 to i16*
  store i16 256, i16* %135, align 1
  call void @llvm.lifetime.start.p0i8(i64 201, i8* %127) #3
  %136 = bitcast [201 x i8]* %20 to i8*
  %137 = add i64 %29, 84
  %138 = inttoptr i64 %137 to i64*
  store i64 0, i64* %138, align 1
  %139 = add i64 %29, 92
  %140 = inttoptr i64 %139 to i64*
  store i64 0, i64* %140, align 1
  %141 = add i64 %29, 100
  %142 = inttoptr i64 %141 to i64*
  store i64 0, i64* %142, align 1
  %143 = add i64 %29, 108
  %144 = inttoptr i64 %143 to i16*
  store i16 256, i16* %144, align 1
  call void @llvm.lifetime.start.p0i8(i64 201, i8* %136) #3
  %145 = bitcast [201 x i8]* %22 to i8*
  %146 = add i64 %29, 118
  %147 = inttoptr i64 %146 to i64*
  store i64 0, i64* %147, align 1
  %148 = add i64 %29, 126
  %149 = inttoptr i64 %148 to i64*
  store i64 0, i64* %149, align 1
  %150 = add i64 %29, 134
  %151 = inttoptr i64 %150 to i64*
  store i64 0, i64* %151, align 1
  %152 = add i64 %29, 142
  %153 = inttoptr i64 %152 to i16*
  store i16 256, i16* %153, align 1
  call void @llvm.lifetime.start.p0i8(i64 201, i8* %145) #3
  %154 = bitcast i32* %i to i8*
  call void @llvm.lifetime.start.p0i8(i64 4, i8* %154) #3
  store i32 0, i32* %i, align 4
  br label %for.cond

for.cond:                                         ; preds = %for.inc, %if.end
  %155 = load i32, i32* %i, align 4
  call void @__sanitizer_cov_trace_const_cmp4(i32 16, i32 %155)
  %cmp19 = icmp slt i32 %155, 16
  br i1 %cmp19, label %for.body, label %for.cond.cleanup

for.cond.cleanup:                                 ; preds = %for.cond
  store i32 5, i32* %cleanup.dest.slot, align 4
  %156 = bitcast i32* %i to i8*
  call void @llvm.lifetime.end.p0i8(i64 4, i8* %156) #3
  br label %for.end

for.body:                                         ; preds = %for.cond
  %157 = load i32, i32* %i, align 4
  %add = add nsw i32 %157, 44
  %idxprom = sext i32 %add to i64
  %arrayidx20 = getelementptr inbounds [201 x i8], [201 x i8]* %14, i64 0, i64 %idxprom
  %158 = ptrtoint i8* %arrayidx20 to i64
  %159 = lshr i64 %158, 3
  %160 = add i64 %159, 2147450880
  %161 = inttoptr i64 %160 to i8*
  %162 = load i8, i8* %161, align 1
  %163 = icmp ne i8 %162, 0
  br i1 %163, label %164, label %169, !prof !33

164:                                              ; preds = %for.body
  %165 = and i64 %158, 7
  %166 = trunc i64 %165 to i8
  %167 = icmp sge i8 %166, %162
  br i1 %167, label %168, label %169

168:                                              ; preds = %164
  call void @__asan_report_load1(i64 %158) #8
  unreachable

169:                                              ; preds = %164, %for.body
  %170 = load i8, i8* %arrayidx20, align 1
  %171 = load i32, i32* %i, align 4
  %idxprom21 = sext i32 %171 to i64
  %arrayidx22 = getelementptr inbounds [201 x i8], [201 x i8]* %18, i64 0, i64 %idxprom21
  %172 = ptrtoint i8* %arrayidx22 to i64
  %173 = lshr i64 %172, 3
  %174 = add i64 %173, 2147450880
  %175 = inttoptr i64 %174 to i8*
  %176 = load i8, i8* %175, align 1
  %177 = icmp ne i8 %176, 0
  br i1 %177, label %178, label %183, !prof !33

178:                                              ; preds = %169
  %179 = and i64 %172, 7
  %180 = trunc i64 %179 to i8
  %181 = icmp sge i8 %180, %176
  br i1 %181, label %182, label %183

182:                                              ; preds = %178
  call void @__asan_report_store1(i64 %172) #8
  unreachable

183:                                              ; preds = %178, %169
  store i8 %170, i8* %arrayidx22, align 1
  br label %for.inc

for.inc:                                          ; preds = %183
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([13 x i32]* @__sancov_gen_.11 to i64), i64 24) to i32*)) #8
  %184 = load i32, i32* %i, align 4
  %inc = add nsw i32 %184, 1
  store i32 %inc, i32* %i, align 4
  br label %for.cond, !llvm.loop !34

for.end:                                          ; preds = %for.cond.cleanup
  %arrayidx23 = getelementptr inbounds [201 x i8], [201 x i8]* %18, i64 0, i64 16
  %185 = ptrtoint i8* %arrayidx23 to i64
  %186 = lshr i64 %185, 3
  %187 = add i64 %186, 2147450880
  %188 = inttoptr i64 %187 to i8*
  %189 = load i8, i8* %188, align 1
  %190 = icmp ne i8 %189, 0
  br i1 %190, label %191, label %196, !prof !33

191:                                              ; preds = %for.end
  %192 = and i64 %185, 7
  %193 = trunc i64 %192 to i8
  %194 = icmp sge i8 %193, %189
  br i1 %194, label %195, label %196

195:                                              ; preds = %191
  call void @__asan_report_store1(i64 %185) #8
  unreachable

196:                                              ; preds = %191, %for.end
  store i8 0, i8* %arrayidx23, align 16
  %197 = bitcast i32* %i24 to i8*
  call void @llvm.lifetime.start.p0i8(i64 4, i8* %197) #3
  store i32 0, i32* %i24, align 4
  br label %for.cond25

for.cond25:                                       ; preds = %for.inc35, %196
  %198 = load i32, i32* %i24, align 4
  call void @__sanitizer_cov_trace_const_cmp4(i32 8, i32 %198)
  %cmp26 = icmp slt i32 %198, 8
  br i1 %cmp26, label %for.body28, label %for.cond.cleanup27

for.cond.cleanup27:                               ; preds = %for.cond25
  store i32 8, i32* %cleanup.dest.slot, align 4
  %199 = bitcast i32* %i24 to i8*
  call void @llvm.lifetime.end.p0i8(i64 4, i8* %199) #3
  br label %for.end37

for.body28:                                       ; preds = %for.cond25
  %200 = load i32, i32* %i24, align 4
  %add29 = add nsw i32 %200, 44
  %add30 = add nsw i32 %add29, 16
  %idxprom31 = sext i32 %add30 to i64
  %arrayidx32 = getelementptr inbounds [201 x i8], [201 x i8]* %14, i64 0, i64 %idxprom31
  %201 = ptrtoint i8* %arrayidx32 to i64
  %202 = lshr i64 %201, 3
  %203 = add i64 %202, 2147450880
  %204 = inttoptr i64 %203 to i8*
  %205 = load i8, i8* %204, align 1
  %206 = icmp ne i8 %205, 0
  br i1 %206, label %207, label %212, !prof !33

207:                                              ; preds = %for.body28
  %208 = and i64 %201, 7
  %209 = trunc i64 %208 to i8
  %210 = icmp sge i8 %209, %205
  br i1 %210, label %211, label %212

211:                                              ; preds = %207
  call void @__asan_report_load1(i64 %201) #8
  unreachable

212:                                              ; preds = %207, %for.body28
  %213 = load i8, i8* %arrayidx32, align 1
  %214 = load i32, i32* %i24, align 4
  %idxprom33 = sext i32 %214 to i64
  %arrayidx34 = getelementptr inbounds [201 x i8], [201 x i8]* %20, i64 0, i64 %idxprom33
  %215 = ptrtoint i8* %arrayidx34 to i64
  %216 = lshr i64 %215, 3
  %217 = add i64 %216, 2147450880
  %218 = inttoptr i64 %217 to i8*
  %219 = load i8, i8* %218, align 1
  %220 = icmp ne i8 %219, 0
  br i1 %220, label %221, label %226, !prof !33

221:                                              ; preds = %212
  %222 = and i64 %215, 7
  %223 = trunc i64 %222 to i8
  %224 = icmp sge i8 %223, %219
  br i1 %224, label %225, label %226

225:                                              ; preds = %221
  call void @__asan_report_store1(i64 %215) #8
  unreachable

226:                                              ; preds = %221, %212
  store i8 %213, i8* %arrayidx34, align 1
  br label %for.inc35

for.inc35:                                        ; preds = %226
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([13 x i32]* @__sancov_gen_.11 to i64), i64 28) to i32*)) #8
  %227 = load i32, i32* %i24, align 4
  %inc36 = add nsw i32 %227, 1
  store i32 %inc36, i32* %i24, align 4
  br label %for.cond25, !llvm.loop !35

for.end37:                                        ; preds = %for.cond.cleanup27
  %arrayidx38 = getelementptr inbounds [201 x i8], [201 x i8]* %20, i64 0, i64 8
  %228 = ptrtoint i8* %arrayidx38 to i64
  %229 = lshr i64 %228, 3
  %230 = add i64 %229, 2147450880
  %231 = inttoptr i64 %230 to i8*
  %232 = load i8, i8* %231, align 1
  %233 = icmp ne i8 %232, 0
  br i1 %233, label %234, label %239, !prof !33

234:                                              ; preds = %for.end37
  %235 = and i64 %228, 7
  %236 = trunc i64 %235 to i8
  %237 = icmp sge i8 %236, %232
  br i1 %237, label %238, label %239

238:                                              ; preds = %234
  call void @__asan_report_store1(i64 %228) #8
  unreachable

239:                                              ; preds = %234, %for.end37
  store i8 0, i8* %arrayidx38, align 8
  %240 = bitcast i32* %i39 to i8*
  call void @llvm.lifetime.start.p0i8(i64 4, i8* %240) #3
  store i32 0, i32* %i39, align 4
  br label %for.cond40

for.cond40:                                       ; preds = %for.inc51, %239
  %241 = load i32, i32* %i39, align 4
  call void @__sanitizer_cov_trace_const_cmp4(i32 4, i32 %241)
  %cmp41 = icmp slt i32 %241, 4
  br i1 %cmp41, label %for.body43, label %for.cond.cleanup42

for.cond.cleanup42:                               ; preds = %for.cond40
  store i32 11, i32* %cleanup.dest.slot, align 4
  %242 = bitcast i32* %i39 to i8*
  call void @llvm.lifetime.end.p0i8(i64 4, i8* %242) #3
  br label %for.end53

for.body43:                                       ; preds = %for.cond40
  %243 = load i32, i32* %i39, align 4
  %add44 = add nsw i32 %243, 44
  %add45 = add nsw i32 %add44, 16
  %add46 = add nsw i32 %add45, 8
  %idxprom47 = sext i32 %add46 to i64
  %arrayidx48 = getelementptr inbounds [201 x i8], [201 x i8]* %14, i64 0, i64 %idxprom47
  %244 = ptrtoint i8* %arrayidx48 to i64
  %245 = lshr i64 %244, 3
  %246 = add i64 %245, 2147450880
  %247 = inttoptr i64 %246 to i8*
  %248 = load i8, i8* %247, align 1
  %249 = icmp ne i8 %248, 0
  br i1 %249, label %250, label %255, !prof !33

250:                                              ; preds = %for.body43
  %251 = and i64 %244, 7
  %252 = trunc i64 %251 to i8
  %253 = icmp sge i8 %252, %248
  br i1 %253, label %254, label %255

254:                                              ; preds = %250
  call void @__asan_report_load1(i64 %244) #8
  unreachable

255:                                              ; preds = %250, %for.body43
  %256 = load i8, i8* %arrayidx48, align 1
  %257 = load i32, i32* %i39, align 4
  %idxprom49 = sext i32 %257 to i64
  %arrayidx50 = getelementptr inbounds [201 x i8], [201 x i8]* %22, i64 0, i64 %idxprom49
  %258 = ptrtoint i8* %arrayidx50 to i64
  %259 = lshr i64 %258, 3
  %260 = add i64 %259, 2147450880
  %261 = inttoptr i64 %260 to i8*
  %262 = load i8, i8* %261, align 1
  %263 = icmp ne i8 %262, 0
  br i1 %263, label %264, label %269, !prof !33

264:                                              ; preds = %255
  %265 = and i64 %258, 7
  %266 = trunc i64 %265 to i8
  %267 = icmp sge i8 %266, %262
  br i1 %267, label %268, label %269

268:                                              ; preds = %264
  call void @__asan_report_store1(i64 %258) #8
  unreachable

269:                                              ; preds = %264, %255
  store i8 %256, i8* %arrayidx50, align 1
  br label %for.inc51

for.inc51:                                        ; preds = %269
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([13 x i32]* @__sancov_gen_.11 to i64), i64 32) to i32*)) #8
  %270 = load i32, i32* %i39, align 4
  %inc52 = add nsw i32 %270, 1
  store i32 %inc52, i32* %i39, align 4
  br label %for.cond40, !llvm.loop !36

for.end53:                                        ; preds = %for.cond.cleanup42
  %arrayidx54 = getelementptr inbounds [201 x i8], [201 x i8]* %22, i64 0, i64 4
  %271 = ptrtoint i8* %arrayidx54 to i64
  %272 = lshr i64 %271, 3
  %273 = add i64 %272, 2147450880
  %274 = inttoptr i64 %273 to i8*
  %275 = load i8, i8* %274, align 1
  %276 = icmp ne i8 %275, 0
  br i1 %276, label %277, label %282, !prof !33

277:                                              ; preds = %for.end53
  %278 = and i64 %271, 7
  %279 = trunc i64 %278 to i8
  %280 = icmp sge i8 %279, %275
  br i1 %280, label %281, label %282

281:                                              ; preds = %277
  call void @__asan_report_store1(i64 %271) #8
  unreachable

282:                                              ; preds = %277, %for.end53
  store i8 0, i8* %arrayidx54, align 4
  %arraydecay55 = getelementptr inbounds [201 x i8], [201 x i8]* %22, i64 0, i64 0
  %call56 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ({ [4 x i8], [60 x i8] }, { [4 x i8], [60 x i8] }* @.str.9, i32 0, i32 0, i64 0), i8* %arraydecay55)
  %283 = bitcast i64* %x to i8*
  call void @llvm.lifetime.start.p0i8(i64 8, i8* %283) #3
  %arraydecay57 = getelementptr inbounds [201 x i8], [201 x i8]* %18, i64 0, i64 0
  %call58 = call i64 @strtoull(i8* %arraydecay57, i8** null, i32 16) #3
  store i64 %call58, i64* %x, align 8
  %284 = load i64, i64* %x, align 8
  call void @__sanitizer_cov_trace_const_cmp8(i64 -3819410105351357762, i64 %284)
  %cmp59 = icmp ne i64 %284, -3819410105351357762
  br i1 %cmp59, label %if.then60, label %if.end61

if.then60:                                        ; preds = %282
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([13 x i32]* @__sancov_gen_.11 to i64), i64 36) to i32*)) #8
  store i32 1, i32* %retval, align 4
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup77

if.end61:                                         ; preds = %282
  %285 = bitcast i32* %y to i8*
  call void @llvm.lifetime.start.p0i8(i64 4, i8* %285) #3
  %arraydecay62 = getelementptr inbounds [201 x i8], [201 x i8]* %20, i64 0, i64 0
  %call63 = call i64 @strtoul(i8* %arraydecay62, i8** null, i32 16) #3
  %conv64 = trunc i64 %call63 to i32
  store i32 %conv64, i32* %y, align 4
  %286 = load i32, i32* %y, align 4
  call void @__sanitizer_cov_trace_const_cmp4(i32 -559038242, i32 %286)
  %cmp65 = icmp ne i32 %286, -559038242
  br i1 %cmp65, label %if.then66, label %if.end67

if.then66:                                        ; preds = %if.end61
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([13 x i32]* @__sancov_gen_.11 to i64), i64 40) to i32*)) #8
  store i32 1, i32* %retval, align 4
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup76

if.end67:                                         ; preds = %if.end61
  %287 = bitcast i16* %z to i8*
  call void @llvm.lifetime.start.p0i8(i64 2, i8* %287) #3
  %arraydecay68 = getelementptr inbounds [201 x i8], [201 x i8]* %22, i64 0, i64 0
  %call69 = call i64 @strtouq(i8* %arraydecay68, i8** null, i32 16) #3
  %conv70 = trunc i64 %call69 to i16
  store i16 %conv70, i16* %z, align 2
  %288 = load i16, i16* %z, align 2
  %conv71 = zext i16 %288 to i32
  %289 = zext i32 %conv71 to i64
  call void @__sanitizer_cov_trace_switch(i64 %289, i64* getelementptr inbounds ([3 x i64], [3 x i64]* @__sancov_gen_cov_switch_values.12, i32 0, i32 0))
  switch i32 %conv71, label %sw.default73 [
    i32 48879, label %sw.bb72
  ]

sw.bb72:                                          ; preds = %if.end67
  br label %sw.epilog74

sw.default73:                                     ; preds = %if.end67
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([13 x i32]* @__sancov_gen_.11 to i64), i64 44) to i32*)) #8
  store i32 1, i32* %retval, align 4
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup

sw.epilog74:                                      ; preds = %sw.bb72
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([13 x i32]* @__sancov_gen_.11 to i64), i64 48) to i32*)) #8
  %call75 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ({ [33 x i8], [63 x i8] }, { [33 x i8], [63 x i8] }* @.str.10, i32 0, i32 0, i64 0))
  store i32 0, i32* %retval, align 4
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup

cleanup:                                          ; preds = %sw.epilog74, %sw.default73
  %290 = bitcast i16* %z to i8*
  call void @llvm.lifetime.end.p0i8(i64 2, i8* %290) #3
  br label %cleanup76

cleanup76:                                        ; preds = %cleanup, %if.then66
  %291 = bitcast i32* %y to i8*
  call void @llvm.lifetime.end.p0i8(i64 4, i8* %291) #3
  br label %cleanup77

cleanup77:                                        ; preds = %cleanup76, %if.then60
  %292 = bitcast i64* %x to i8*
  call void @llvm.lifetime.end.p0i8(i64 8, i8* %292) #3
  %293 = bitcast [201 x i8]* %22 to i8*
  %294 = add i64 %29, 118
  %295 = inttoptr i64 %294 to i64*
  store i64 -506381209866536712, i64* %295, align 1
  %296 = add i64 %29, 126
  %297 = inttoptr i64 %296 to i64*
  store i64 -506381209866536712, i64* %297, align 1
  %298 = add i64 %29, 134
  %299 = inttoptr i64 %298 to i64*
  store i64 -506381209866536712, i64* %299, align 1
  %300 = add i64 %29, 142
  %301 = inttoptr i64 %300 to i16*
  store i16 -1800, i16* %301, align 1
  call void @llvm.lifetime.end.p0i8(i64 201, i8* %293) #3
  %302 = bitcast [201 x i8]* %20 to i8*
  %303 = add i64 %29, 84
  %304 = inttoptr i64 %303 to i64*
  store i64 -506381209866536712, i64* %304, align 1
  %305 = add i64 %29, 92
  %306 = inttoptr i64 %305 to i64*
  store i64 -506381209866536712, i64* %306, align 1
  %307 = add i64 %29, 100
  %308 = inttoptr i64 %307 to i64*
  store i64 -506381209866536712, i64* %308, align 1
  %309 = add i64 %29, 108
  %310 = inttoptr i64 %309 to i16*
  store i16 -1800, i16* %310, align 1
  call void @llvm.lifetime.end.p0i8(i64 201, i8* %302) #3
  %311 = bitcast [201 x i8]* %18 to i8*
  %312 = add i64 %29, 50
  %313 = inttoptr i64 %312 to i64*
  store i64 -506381209866536712, i64* %313, align 1
  %314 = add i64 %29, 58
  %315 = inttoptr i64 %314 to i64*
  store i64 -506381209866536712, i64* %315, align 1
  %316 = add i64 %29, 66
  %317 = inttoptr i64 %316 to i64*
  store i64 -506381209866536712, i64* %317, align 1
  %318 = add i64 %29, 74
  %319 = inttoptr i64 %318 to i16*
  store i16 -1800, i16* %319, align 1
  call void @llvm.lifetime.end.p0i8(i64 201, i8* %311) #3
  br label %cleanup81

cleanup81:                                        ; preds = %cleanup77, %if.then
  %320 = bitcast [45 x i8]* %16 to i8*
  %321 = add i64 %29, 40
  %322 = inttoptr i64 %321 to i32*
  store i32 -117901064, i32* %322, align 1
  %323 = add i64 %29, 44
  %324 = inttoptr i64 %323 to i16*
  store i16 -1800, i16* %324, align 1
  call void @llvm.lifetime.end.p0i8(i64 45, i8* %320) #3
  %325 = bitcast %struct._IO_FILE** %fp to i8*
  call void @llvm.lifetime.end.p0i8(i64 8, i8* %325) #3
  %326 = bitcast [201 x i8]* %14 to i8*
  %327 = add i64 %29, 6
  %328 = inttoptr i64 %327 to i64*
  store i64 -506381209866536712, i64* %328, align 1
  %329 = add i64 %29, 14
  %330 = inttoptr i64 %329 to i64*
  store i64 -506381209866536712, i64* %330, align 1
  %331 = add i64 %29, 22
  %332 = inttoptr i64 %331 to i64*
  store i64 -506381209866536712, i64* %332, align 1
  %333 = add i64 %29, 30
  %334 = inttoptr i64 %333 to i16*
  store i16 -1800, i16* %334, align 1
  call void @llvm.lifetime.end.p0i8(i64 201, i8* %326) #3
  %335 = bitcast i8** %filename to i8*
  call void @llvm.lifetime.end.p0i8(i64 8, i8* %335) #3
  %336 = bitcast i32* %12 to i8*
  %337 = add i64 %29, 4
  %338 = inttoptr i64 %337 to i8*
  store i8 -8, i8* %338, align 1
  call void @llvm.lifetime.end.p0i8(i64 4, i8* %336) #3
  %339 = bitcast i32* %opt to i8*
  call void @llvm.lifetime.end.p0i8(i64 4, i8* %339) #3
  %340 = load i32, i32* %retval, align 4
  store i64 1172321806, i64* %23, align 8
  %341 = icmp ne i64 %5, 0
  br i1 %341, label %342, label %343

342:                                              ; preds = %cleanup81
  call void @__asan_stack_free_5(i64 %5, i64 1216)
  br label %345

343:                                              ; preds = %cleanup81
  %344 = add i64 %29, 0
  call void @__asan_set_shadow_00(i64 %344, i64 152)
  br label %345

345:                                              ; preds = %343, %342
  ret i32 %340
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
  call void @__asan_before_dynamic_init(i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64))
  call void @__sanitizer_cov_trace_pc_guard(i32* getelementptr inbounds ([1 x i32], [1 x i32]* @__sancov_gen_.13, i32 0, i32 0)) #8
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
  call void @__asan_before_dynamic_init(i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64))
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
  call void @__asan_register_globals(i64 ptrtoint ([13 x { i64, i64, i64, i64, i64, i64, i64, i64 }]* @0 to i64), i64 13)
  ret void
}

declare void @__asan_version_mismatch_check_v8()

define internal void @asan.module_dtor() {
  call void @__asan_unregister_globals(i64 ptrtoint ([13 x { i64, i64, i64, i64, i64, i64, i64, i64 }]* @0 to i64), i64 13)
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

!llvm.asan.globals = !{!3, !5, !7, !9, !11, !13, !15, !17, !19, !21, !23, !25, !27}
!llvm.module.flags = !{!29}
!llvm.ident = !{!30}

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
!15 = !{[27 x i8]* getelementptr inbounds ({ [27 x i8], [37 x i8] }, { [27 x i8], [37 x i8] }* @.str.4, i32 0, i32 0), !16, !"<string literal>", i1 false, i1 false}
!16 = !{!"demo/demo.cc", i32 46, i32 12}
!17 = !{[21 x i8]* getelementptr inbounds ({ [21 x i8], [43 x i8] }, { [21 x i8], [43 x i8] }* @.str.5, i32 0, i32 0), !18, !"<string literal>", i1 false, i1 false}
!18 = !{!"demo/demo.cc", i32 52, i32 28}
!19 = !{[12 x i8]* getelementptr inbounds ({ [12 x i8], [52 x i8] }, { [12 x i8], [52 x i8] }* @.str.6, i32 0, i32 0), !20, !"<string literal>", i1 false, i1 false}
!20 = !{!"demo/demo.cc", i32 53, i32 30}
!21 = !{[14 x i8]* getelementptr inbounds ({ [14 x i8], [50 x i8] }, { [14 x i8], [50 x i8] }* @.str.7, i32 0, i32 0), !22, !"<string literal>", i1 false, i1 false}
!22 = !{!"demo/demo.cc", i32 54, i32 29}
!23 = !{[27 x i8]* getelementptr inbounds ({ [27 x i8], [37 x i8] }, { [27 x i8], [37 x i8] }* @.str.8, i32 0, i32 0), !24, !"<string literal>", i1 false, i1 false}
!24 = !{!"demo/demo.cc", i32 58, i32 12}
!25 = !{[4 x i8]* getelementptr inbounds ({ [4 x i8], [60 x i8] }, { [4 x i8], [60 x i8] }* @.str.9, i32 0, i32 0), !26, !"<string literal>", i1 false, i1 false}
!26 = !{!"demo/demo.cc", i32 73, i32 12}
!27 = !{[33 x i8]* getelementptr inbounds ({ [33 x i8], [63 x i8] }, { [33 x i8], [63 x i8] }* @.str.10, i32 0, i32 0), !28, !"<string literal>", i1 false, i1 false}
!28 = !{!"demo/demo.cc", i32 95, i32 12}
!29 = !{i32 1, !"wchar_size", i32 4}
!30 = !{!"clang version 12.0.1 (git@github.com:fengzhengzhan/BTFuzz.git 0b64f5806b4302732328fa068687800669443ef8)"}
!31 = distinct !{!31, !32}
!32 = !{!"llvm.loop.mustprogress"}
!33 = !{!"branch_weights", i32 1, i32 100000}
!34 = distinct !{!34, !32}
!35 = distinct !{!35, !32}
!36 = distinct !{!36, !32}
